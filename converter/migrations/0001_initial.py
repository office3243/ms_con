# Generated by Django 2.2 on 2019-08-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_file_url', models.URLField()),
                ('input_file', models.FileField(upload_to='files/input_files/')),
                ('output_file', models.FileField(blank=True, null=True, upload_to='files/output_files/')),
                ('input_file_type', models.CharField(blank=True, choices=[('ppt', 'PPT'), ('pptx', 'PPTX'), ('doc', 'DOC'), ('docx', 'DOCX'), ('xls', 'XLS'), ('xlsx', 'XLSX')], default='pptx', max_length=3)),
                ('is_converted', models.BooleanField(default=False)),
                ('has_errors', models.BooleanField(default=False)),
            ],
        ),
    ]
