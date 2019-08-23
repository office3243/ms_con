from django.db import models
from . import converters
from django.conf import settings


class FileObject(models.Model):

    OUTPUT_FILES_PATH = "files/output_files/"
    INPUT_FILES_PATH = "files/input_files/"

    FILE_TYPE_CHOICES = (("ppt", "PPT"), ("pptx", "PPTX"), ("doc", "DOC"), ("docx", "DOCX"), ("xls", "XLS"),
                         ("xlsx", "XLSX"))

    input_file = models.FileField(upload_to=INPUT_FILES_PATH, blank=True, null=True)
    output_file = models.FileField(upload_to=OUTPUT_FILES_PATH, blank=True, null=True)
    input_file_type = models.CharField(max_length=5, choices=FILE_TYPE_CHOICES, blank=True)
    is_converted = models.BooleanField(default=False)
    has_errors = models.BooleanField(default=False)

    def __str__(self):
        return str(self.get_file_pure_name)
    
    @property
    def get_output_file_url(self):
        return settings.SITE_DOMAIN + self.output_file.url

    @property
    def get_input_file_absolute_path(self):
        return self.input_file.path

    @property
    def get_converted_file_absolute_path(self):
        return str(settings.MEDIA_ROOT).replace("\\", "/") + self.get_file_pure_name + ".pdf"

    @property
    def get_converted_file_relative_path(self):
        return self.OUTPUT_FILES_PATH + self.get_file_pure_name + ".pdf"

    @property
    def get_file_pure_name(self):
        raw_name = self.input_file.name
        return raw_name[raw_name.rfind("/")+1: raw_name.rfind(".")]

    def convert_file(self):
        output = converters.convert_file(input_file_absolute_path=self.get_input_file_absolute_path,
                                         output_file_absolute_path=self.get_converted_file_absolute_path,
                                         input_file_type=self.input_file_type)
        if output:
            self.output_file = self.get_converted_file_relative_path
            self.is_converted = True
            self.save()
        else:
            self.has_errors = True
            self.save()

    def save(self, *args, **kwargs):
        if self.input_file and not self.is_converted and not self.has_errors:
            self.convert_file()
        super().save()
