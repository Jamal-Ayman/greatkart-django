# Generated by Django 3.1 on 2021-10-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210914_1755'),
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='product_category',
            field=models.ManyToManyField(blank=True, to='category.Category'),
        ),
    ]
