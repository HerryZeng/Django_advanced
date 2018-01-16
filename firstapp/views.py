from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

def home(request):
    user_list = User.objects.all()
    return render(request, 'firstapp/table.html', locals())
