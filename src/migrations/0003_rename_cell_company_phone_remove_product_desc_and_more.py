# Generated by Django 4.0.2 on 2022-07-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_alter_carroussel_background_alter_company_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='cell',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
