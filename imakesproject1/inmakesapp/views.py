from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def demo(request):
#     name='linus'
#     return render (request,'index.html',{'obj':name})
from inmakesapp.models import place,team


def demo(request):
    obj=place.objects.all()
    obj2 = team.objects.all()
    return render (request,'index.html',{'result':obj,'result2':obj2})

# def innerpage(request):
#     return render (request,'inner-page.html')
# def contact(request):
#     return render (request,'contact.html')

