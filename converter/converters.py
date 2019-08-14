import win32com.client as win_client
import pythoncom
from django.conf import settings


#   DOC TO PDF
#
def doc_to_pdf(input_file, absolute_path):

    try:
        pythoncom.CoInitialize()
        word = win_client.Dispatch('Word.Application')
        doc = word.Documents.Open(input_file)
        doc.SaveAs(absolute_path, FileFormat=17)
        doc.Close()
        word.Quit()
        return True
    except Exception as e:
        print(e)
        return False


#   PPT TO PDF

def ppt_to_pdf(input_file, absolute_path, formatType=32):
    try:
        pythoncom.CoInitialize()
        powerpoint = win_client.Dispatch("Powerpoint.Application")
        powerpoint.Visible = 1
        deck = powerpoint.Presentations.Open(input_file)
        deck.SaveAs(absolute_path, formatType)
        deck.Close()
        powerpoint.Quit()
        return True
    except Exception as e:
        print(e)
        return False


#   XLS TO PDF


def xls_to_pdf(input_file, absolute_path):
    try:
        pythoncom.CoInitialize()
        xlApp = win_client.Dispatch("Excel.Application")
        books = xlApp.Workbooks.Open(input_file)
        ws = books.Worksheets[0]
        ws.Visible = 1
        ws.ExportAsFixedFormat(0, absolute_path)
        return True
    except Exception as e:
        print(e)
        return False
