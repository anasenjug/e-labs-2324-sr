from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:image_id>/', views.detail, name="detail"),
    path("new/", views.create_image, name="create_image"),
    path('<int:image_id>/comments/new/', views.post_comment, name="post_comment"),
]
