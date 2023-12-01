from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Image

# Create your views here.
def homepage(request):
    count = Image.objects.count()
    context={
        "count":count,

    }
    return render(request,'images/homepage.html',context)

def image_list(request):
    images=Image.objects.all()
    context={
        "images":images,
    }
    return render(request,'images/image_list.html',context)

def image_detail(request,image_id):
    image = get_object_or_404(Image,pk=image_id)
    context={
        "image":image,
    }
    return render(request, 'images/image_detail.html',context)

def image_create(request):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        url=request.POST['url']
        created_at=request.POST['created_at']
        image=Image(
            title=title,
            desc=desc,
            url=url,
            created_at=created_at
        )
        image.save()
        return HttpResponseRedirect(reverse('image_detail',args=(image.id,)))

    context={}
    return render(request,'images/image_create.html',context)