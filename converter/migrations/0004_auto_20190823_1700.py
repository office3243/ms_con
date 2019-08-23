# Generated by Django 2.2 on 2019-08-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_remove_fileobject_input_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileobject',
            name='input_file_type',
            field=models.CharField(blank=True, choices=[('ppt', 'PPT'), ('pptx', 'PPTX'), ('doc', 'DOC'), ('docx', 'DOCX'), ('xls', 'XLS'), ('xlsx', 'XLSX')], default='pptx', max_length=5),
        ),
    ]
