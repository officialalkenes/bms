# Generated by Django 5.1.2 on 2024-10-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_remove_category_cat_num_remove_category_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
