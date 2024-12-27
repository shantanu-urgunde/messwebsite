from . import views
from django.urls import path

app_name = "suggestions"
urlpatterns = [
    path("", views.index, name = "index")
]