# Generated by Django 5.0.4 on 2024-05-01 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_student_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
    ]
