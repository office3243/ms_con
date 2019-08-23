from django.db import models
from . import converters
from django.conf import settings


class FileObject(models.Model):

    OUTPUT_FILES_PATH = "files/output_files/"
    INPUT_FILES_PATH = "files/input_files/"

    FILE_TYPE_CHOICES = (("ppt", "PPT"), ("pptx", "PPTX"), ("doc", "DOC"), ("docx", "DOCX"), ("xls", "XLS"),
                         ("xlsx", "XLSX"))

    input_file_url = models.URLField()
    input_file = models.FileField(upload_to=INPUT_FILES_PATH, blank=True, null=True)
    output_file = models.FileField(upload_to=OUTPUT_FILES_PATH, blank=True, null=True)
    input_file_type = models.CharField(max_length=3, choices=FILE_TYPE_CHOICES, blank=True, default="pptx")
    is_converted = models.BooleanField(default=False)
    has_errors = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_output_file_url(self):
        return settings.SITE_DOMAIN + self.output_file.url

    @property
    def get_input_file_absolute_path(self):
        print(self.input_file.path)
        return str(settings.MEDIA_ROOT).replace("\\", "/") + self.input_file.path

    @property
    def get_converted_file_absolute_path(self):
        return str(settings.MEDIA_ROOT).replace("\\", "/") + self.OUTPUT_FILES_PATH + self.get_file_name + ".pdf"

    @property
    def get_converted_file_relative_path(self):
        return self.OUTPUT_FILES_PATH + self.get_file_name + ".pdf"

    @property
    def get_file_name(self):
        return self.input_file_url[self.input_file_url.rfind("/")+1:self.input_file_url.rfind(".")]

    def convert_file(self):
        print("Convert")
        # if self.input_file_type in ("ppt", "pptx"):
        #     print("PPT")
        #     print(self.get_input_file_absolute_path)
        #     output = converters.ppt_to_pdf(input_file=self.get_input_file_absolute_path,
        #                                    absolute_path=self.get_converted_file_absolute_path)
        #
        # elif self.input_file_type in ("doc", "docx"):
        #     output = converters.doc_to_pdf(input_file=self.input_file_url,
        #                                    absolute_path=self.get_converted_file_absolute_path)
        #
        # elif self.input_file_type in ("xls", "xlsx"):
        #     output = converters.xls_to_pdf(input_file=self.input_file_url,
        #                                    absolute_path=self.get_converted_file_absolute_path)
        # else:
        #     print("else")
        #     output = False
        # print(output)
        # if not output:
        #     self.has_errors = True
        #     self.save()
        # else:
        #     self.output_file = self.get_converted_file_relative_path
        #     self.is_converted = True
        #     self.save()
        return True

    def save(self, *args, **kwargs):
        print(self.input_file)
        if self.input_file is not None and not self.is_converted and not self.has_errors:
            print("IF----------------")
            self.convert_file()
        super().save()
