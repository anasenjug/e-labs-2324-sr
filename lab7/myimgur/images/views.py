from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

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
    comments = image.comment_set.all()
    #comments=Comment.objects.filter(image=image)
    context = {
        "image": image,
        "comments":comments,
    }
    return render(request, 'images/image_detail.html', context)

def image_create(request):
    if request.method== "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        pub_date=request.POST['pub_date']
        url=request.POST['url']
        image=Image(
            title=title,
            desc=desc,
            pub_date=pub_date,
            url=url
        )
        image.save()
        return HttpResponseRedirect(f"/images/{image.id}/")
    context={}
    return render(request,'images/image_create.html',context)

def comment_create(request,image_id):
    if request.method == "POST":
        image = get_object_or_404(Image, pk=image_id)
        author = request.POST['author']
        text = request.POST['text']
        image.comment_set.create(
            author = author,
            text = text,
        )

    return HttpResponseRedirect(f"/images/{image_id}")