from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .functions import get_date

heading = "Personīgā dienasgrāmata"
#================================================================================================
#================================================================================================
#================================================================================================
def blogs(request): 
   
   posts = Post.objects.order_by('-id') # No datubāzes visus ierakstus 

   logo = "Basma.lv"

   heading = "Personīgā dienasgrāmata"

   subHeading = "Tā cilvēks daudz labāk saprot dzīves un viņa paša jēgu."

   date = get_date()

   context = {
       'date' : date,
       'posts' : posts,
       'logo' : logo,
       'heading' : heading,
       'subheading' : subHeading
   }
   return render(request, "index.html", context = context)

#================================================================================================
#================================================================================================
#================================================================================================
def post_detail(request, id):

    post = Post.objects.get(id=id)

    subHeading = post.title

    logo = "Basma.lv"

    data = {
        'post' : post,
        'logo' : logo,
        'heading' : heading,
        'subheading' : subHeading
    }

    return render(request, 'post.html', context=data)

#================================================================================================
#================================================================================================
#================================================================================================
def home(request):
    return HttpResponse("Sveiki, šis ir mājaslapas saturs!")

#================================================================================================
#================================================================================================
#================================================================================================
# "Špikeris"

def cheatsheet(requests):

    logo = "Basma.lv"

    subHeading = "Špikeris - mazais palīgs, lai lielas idejas nekad neaizmirstu!"

    data = {
        'logo' : logo,
        'heading' : heading,
        'subheading' : subHeading
    }

    return render(requests, "cheatsheet.html", context=data)