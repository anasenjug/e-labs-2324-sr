from django.urls import path
from .views import image_list,image_detail, image_create

urlpatterns = [
    path('',image_list,name="image_list"),
    path('<int:image_id>/',image_detail,name="image_detail"),
    path('new/',image_create,name="image_create"),
]
