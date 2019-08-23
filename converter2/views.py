from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse
from . import converters
from django.views.decorators.csrf import csrf_exempt
from .models import FileObject
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
from django.conf import settings
from .forms import FileObjectAddForm


@csrf_exempt
def convert_file_view(request):
    if request.method == "POST":
        file_data = request.FILES['input_file']
        file = FileObject.objects.create(input_file_type="pptx")

        print(file.id)

        # file.input_file.save("abced.pptx", file_data, save=True)
        # file.save()

        print("file saved")
        print(file.input_file.url)
        if file.is_converted:
            with open(file.get_converted_file_absolute_path, "rb") as f:
                file_data = f.read()
                f.close()
            response = HttpResponse(file_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(file.get_file_name)
            response['is_converted'] = True
            return response
        else:
            response = HttpResponse()
            response['is_converted'] = False
            return response
    else:
        return render(request, "form.html", {'form': FileObjectAddForm()})
        # raise Http404("Bad Request")
#

#
# @csrf_exempt
# def convert_file_view(request):
#     if request.method == "POST":
#         print(request.FILES)
#         print(vars(request.FILES))
#         file_url = request.POST.get("file_url")
#         # file_type = file_url[file_url.rfind(".") + 1:].lower()
#         # file = FileObject.objects.create(input_file_url=file_url, input_file_type=file_type)
#         # file_ext = request.headers['file_ext']
#         file_ext = "pptx"
#         req_file_path = str(settings.MEDIA_ROOT).replace("\\", "/") + FileObject.INPUT_FILES_PATH + str(uuid.uuid4()) + "." + file_ext
#         open(req_file_path, "wb").write(request.content)
#         file = FileObject.objects.create(input_file=req_file_path, input_file_type=file_ext)
#         if file.is_converted:
#             with open(file.get_converted_file_absolute_path, "rb") as f:
#                 file_data = f.read()
#                 f.close()
#             response = HttpResponse(file_data, content_type='application/pdf')
#             response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(file.get_file_name)
#             response['is_converted'] = True
#             return response
#         else:
#             response = HttpResponse()
#             response['is_converted'] = False
#             return response
#     else:
#         raise Http404("Bad Request")
