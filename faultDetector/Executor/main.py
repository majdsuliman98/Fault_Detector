from .BaseDetectorAlgorithm import BaseDetectorAlgorithm
import threading
import mysql.connector
import os
import queue
import sys
sys.path.append("./media/Algorithms")


def runAlgorithms(algorithm, dataset, resultQueue):
    print(os.listdir(os.curdir))   
    PATH_DATASET = f'media/Datasets/{dataset}'
    print(f"Detection faults at {dataset}")
    print(f"Algorithm:{algorithm}")
    try:
        AlgorithmModule = __import__(algorithm)
        getAlgorithmClassname = getattr(AlgorithmModule,"getAlgorithmClassName")
        Algorithm = getattr(AlgorithmModule,getAlgorithmClassname())
        algorithmInstance = Algorithm()
        isValidAlgorithm = isinstance(algorithmInstance,BaseDetectorAlgorithm)
        # if not isValidAlgorithm:
        #     return Exception("Invalid algorithm provided (Has to be child of BaseDetectorAlgorithm) - " + getAlgorithmClassname())
        executor = Algorithm()
        thread = threading.Thread(target = executor.read, args=(PATH_DATASET,))
        thread.start()
        thread.join()
        faultRecords = executor.writeback()
        lenFaultRecord = len(faultRecords)
    
        resultQueue.put((algorithm, dataset, lenFaultRecord))


    except Exception as e:  # catch all exceptions
        print(f"An error occurred while running the algorithm {algorithm}: {e}")


def runAnalysis(algorithms, datasets):
    result_queue = queue.Queue()
    threads = []

    for dataset in datasets:
        for alg in algorithms:
            thread = threading.Thread(target=runAlgorithms, args=(alg, dataset, result_queue))
            threads.append(thread)
            thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Now all threads have finished, start the insertion process
    db_config = {
        'database': 'mydb2',
        'user': 'root',
        'password': 'Majd2000',
        'host': '127.0.0.1',
    }
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    while not result_queue.empty():
        algorithm, dataset, lenFaultRecord = result_queue.get()
        try:
            print(algorithm,dataset,lenFaultRecord)
            query = (
                    f"INSERT INTO FaultRegistry (sourceDatasetId, detectionAlgorithm, faultyRecord) "
                    f"VALUES ((SELECT id FROM SourceDataset WHERE name = '{dataset.split('.')[0]}'), '{algorithm}', '{lenFaultRecord}') "
                    f"ON DUPLICATE KEY UPDATE "
                    f"faultyRecord = '{lenFaultRecord}'"
)


            cursor.execute(query)
            connection.commit()
            print("Inserted for", algorithm, dataset)

        except Exception as e:
            print(e)

    cursor.close()
    connection.close()
    print("Insertion completed")
