# Generated by Django 4.0.2 on 2022-07-15 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_remove_service_icon_alter_whyus_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='src.company'),
        ),
    ]
