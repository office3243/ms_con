import win32com.client as win_client
import pythoncom
from django.conf import settings


#   DOC TO PDF
#
def doc_to_pdf(input_file_absolute_path, output_file_absolute_path):

    try:
        pythoncom.CoInitialize()
        word = win_client.Dispatch('Word.Application')
        doc = word.Documents.Open(input_file_absolute_path)
        doc.SaveAs(output_file_absolute_path, FileFormat=17)
        doc.Close()
        word.Quit()
        return True
    except Exception as e:
        print(e)
        return False


#   PPT TO PDF

def ppt_to_pdf(input_file_absolute_path, output_file_absolute_path, formatType=32):
    try:
        pythoncom.CoInitialize()
        powerpoint = win_client.Dispatch("Powerpoint.Application")
        powerpoint.Visible = 1
        deck = powerpoint.Presentations.Open(input_file_absolute_path)
        deck.SaveAs(output_file_absolute_path, formatType)
        deck.Close()
        powerpoint.Quit()
        return True
    except Exception as e:
        print(e)
        return False


#   XLS TO PDF


def xls_to_pdf(input_file_absolute_path, output_file_absolute_path):
    try:
        pythoncom.CoInitialize()
        xlApp = win_client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(input_file_absolute_path)
        ws = books.Worksheets[0]
        ws.Visible = 1
        ws.ExportAsFixedFormat(0, output_file_absolute_path)
        return True
    except Exception as e:
        print(e)
        return False


def convert_file(input_file_absolute_path, output_file_absolute_path, input_file_type):
    if input_file_type in ("ppt", "pptx"):
        output = ppt_to_pdf(input_file_absolute_path=input_file_absolute_path,
                            output_file_absolute_path=output_file_absolute_path)

    elif input_file_type in ("doc", "docx"):
        output = doc_to_pdf(input_file_absolute_path=input_file_absolute_path,
                            output_file_absolute_path=output_file_absolute_path)

    elif input_file_type in ("xls", "xlsx"):
        output = xls_to_pdf(input_file_absolute_path=input_file_absolute_path,
                            output_file_absolute_path=output_file_absolute_path)
    else:
        output = False
    if output:
        return True
    return False
