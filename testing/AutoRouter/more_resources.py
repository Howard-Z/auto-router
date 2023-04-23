from django.shortcuts import render

def more_resources(request):
    return render(request, 'more_resources.html')