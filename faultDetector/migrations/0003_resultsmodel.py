# Generated by Django 4.1.7 on 2023-08-05 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faultDetector", "0002_algorithmmodel_datasetmodel_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResultsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("executedAlgorithm", models.CharField(max_length=45)),
                ("time", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={"db_table": "Results",},
        ),
    ]
