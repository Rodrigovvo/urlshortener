import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.checks import Error

from .models import Url

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        if len(request.POST['link']) != 0:
            link = request.POST['link']
            uid = str(uuid.uuid4())[:7]
            new_url = Url(link=link,uuid=uid)
            new_url.save()
            return HttpResponse(uid)
        else:
            return Error('Site not found - Blank Argument')

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
