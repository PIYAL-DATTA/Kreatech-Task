from django.shortcuts import *
from django.http import *
from .models import *

# Create your views here.


def home(request):
    return render(request, 'ERMapp/index.html')


def roles(request):
    role = request.POST.get('role')
    roleTable = Post.objects.all()
    for x in roleTable:
        if role == x.role:
            context = {'values': Post.objects.filter(role=role).values()}
            return render(request, 'ERMapp/index.html', context)
    return HttpResponse("Doesn't Exist")


def candidates(request):
    name = request.POST.get('name')
    candidateTable = Candidate.objects.all()
    for x in candidateTable:
        if name == x.name:
            context = {'candidate': Candidate.objects.filter(name=name).values()}
            return render(request, 'ERMapp/index.html', context)
    return HttpResponse("Doesn't Exist")