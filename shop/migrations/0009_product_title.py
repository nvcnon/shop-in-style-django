# Generated by Django 5.2 on 2025-05-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
