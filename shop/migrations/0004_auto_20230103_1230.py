# Generated by Django 2.2 on 2023-01-03 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='catagory',
            new_name='category',
        ),
    ]
