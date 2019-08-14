from django.conf.urls import url
from . import views

app_name = "converter"

urlpatterns = [
    url(r"^convert/$", views.convert_file_view, name="convert"),
]
