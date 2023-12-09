from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Comment
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'images/home.html', context)

def index(request):
    images = Image.objects.all()
    context = {
        'image_list': images
    }
    return render(request, 'images/list.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comments = image.comment_set.all()
    context = {
        'image': image,
        'comments' : comments
    }
    return render(request, 'images/detail.html', context)

def create_image(request):
    if request.method == "POST":
        title = request.POST['title']
        url = request.POST['url']
        pub_date = request.POST['pub_date']

        image = Image(title=title, url=url, pub_date=pub_date)
        image.save()
        return HttpResponseRedirect(reverse("app:detail", args=[image.id,]))

    return render(request, 'images/new.html')


def post_comment(request, image_id):
    if request.method == "POST" and request.user.is_authenticated:
        image = get_object_or_404(Image, pk=image_id)
        comment = Comment(
            user=request.user,
            text=request.POST['text'], 
            image = image, 
            pub_date=timezone.now()
        )
        comment.save()

    return HttpResponseRedirect(reverse("app:detail", args=[image_id]))

