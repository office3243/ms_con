from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FileObject


@csrf_exempt
def convert_file_view(request):
    if request.method == "POST":
        input_file_type = request.POST['file_ext'].lower()
        file_data = request.FILES['input_file']
        file_pure_name = request.POST['file_name']
        file = FileObject.objects.create(input_file_type=input_file_type)
        file.input_file.save(file_pure_name, file_data, save=True)

        if file.is_converted:
            with open(file.get_converted_file_absolute_path, "rb") as f:
                file_data = f.read()
                f.close()
            response = HttpResponse(file_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(file.get_file_pure_name)
            response['is_converted'] = True
            return response
        else:
            response = HttpResponse()
            response['is_converted'] = False
            return response
    else:
        raise Http404("Bad Request")
