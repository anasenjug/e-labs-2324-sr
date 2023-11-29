from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import Image
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def homepage(request):
    count = Image.objects.count()
    context = {
        "count": count,
    }
    return render(request,'images/homepage.html', context)

def image_list(request):
    images = Image.objects.all()
    context = {
        "images": images,
    }
    return render(request, 
                'images/image_list.html', 
                context)

def image_detail(request, image_id):
    image = Image.objects.get(id=image_id)
    comments = image.comment_set.all()
    context = {
        "image": image,
        "comments": comments,
    }
    return render(request,
                  'images/image_detail.html',
                  context
                )

def create_image(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title', "")
        url = request.POST.get("url", "")
        pub_date = request.POST.get("pub_date", 
                           timezone.now())
        desc = request.POST.get("desc", "")
        image = Image(title=title,
                      desc=desc,
                      pub_date=pub_date,
                      url=url)
        image.save()
        return HttpResponseRedirect(
            reverse('images:detail', args=(image.id,))
        )
        

    context = {}
    return render(request,
                 "images/create_image.html",
                 context)
                