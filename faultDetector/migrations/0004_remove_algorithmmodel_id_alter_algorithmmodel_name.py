# Generated by Django 4.1.7 on 2023-08-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faultDetector", "0003_resultsmodel"),
    ]

    operations = [
        migrations.RemoveField(model_name="algorithmmodel", name="id",),
        migrations.AlterField(
            model_name="algorithmmodel",
            name="name",
            field=models.CharField(max_length=45, primary_key=True, serialize=False),
        ),
    ]