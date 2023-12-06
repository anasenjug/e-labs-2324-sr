from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Image

# Create your views here.
def homepage(request):
    images_count = Image.objects.count()
    context = {
        "count": images_count,
    }
    return render(request, 'images/homepage.html', context)

def image_list(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'images/image_list.html', context)

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    context = {
        "image": image,
    }
    return render(request, 'images/image_detail.html', context)
