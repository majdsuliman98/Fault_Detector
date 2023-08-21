# A system for testing fault recognition algorithms
## Getting Started

Follow these steps to run the app:

1. **Setup the Database:**
   Navigate to the `db` directory:
   ```sh
   cd db
2. Run the following command:
    ```sh
    docker-compose up 
    ```
3. go back to the root directory
4. Start the application 
    ```sh
    python3 manage.py runserver
    ```
5. Download the required packages

## Accessing DB
1. Once the docker container up and running
    ```sh
    docker ps -a 
    docker exec -it <ContainerID> /bin/bash
    ```
3. Then run **mysql** however once it asks for the password you should be able to find it in **db/.env**:
    ```sh
    mysql -u root -p 
    ```



