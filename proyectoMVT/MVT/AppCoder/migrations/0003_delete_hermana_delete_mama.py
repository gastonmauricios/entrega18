# Generated by Django 4.1.3 on 2022-12-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_hermana_edad_alter_mama_edad_alter_papa_edad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hermana',
        ),
        migrations.DeleteModel(
            name='Mama',
        ),
    ]