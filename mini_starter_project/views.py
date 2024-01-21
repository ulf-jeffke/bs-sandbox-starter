from django.shortcuts import render

def index(request):
    """The Home Page for mini starter project"""
    return render(request, 'mini_starter_project/index.html')
