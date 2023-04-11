
from django.shortcuts import render
from app import forms

def index (request):
    context = {'form': forms.UniversityForm() }
    return render(request,'index.html',context)
