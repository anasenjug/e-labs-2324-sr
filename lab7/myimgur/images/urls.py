from django.urls import path

from .views import (
    image_list, 
    image_detail, 
    image_create,
    comment_create,
)
app_name="images"
urlpatterns = [
    path('', image_list, name="list"),
    path('<int:image_id>/', image_detail, name="detail"),
    path('new/', image_create, name="create"),
    path('<int:image_id>/comments/new/',comment_create,name="comment_create"),
]