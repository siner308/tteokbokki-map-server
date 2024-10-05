# Generated by Django 3.2.2 on 2024-10-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0003_alter_hashtag_table'),
        ('brand', '0006_auto_20210727_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='hashtags',
            field=models.ManyToManyField(blank=True, db_table='brand_hashtags', to='hashtag.Hashtag'),
        ),
        migrations.AlterModelTable(
            name='brand',
            table='brand',
        ),
    ]