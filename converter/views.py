from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse
from . import converters
from django.views.decorators.csrf import csrf_exempt
from .models import FileObject


@csrf_exempt
def convert_file_view(request):
    if request.method == "POST":
        print(request.POST)
        file_url = request.POST.get("file_url")
        file_type = file_url[file_url.rfind(".") + 1:]
        file = FileObject.objects.create(input_file_url=file_url, input_file_type=file_type)
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
        raise Http404("Bad Request")

