from django.shortcuts import render, redirect

def home(request):
    return render(request,"index.html")

def courses(request):
    return render(request, "courses.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def events(request):
    return render(request,"events.html")

def pricing(request):
    return render(request,"pricing.html")

def trainers(request):
    return render(request,"trainers.html")

def services(request):
    return render(request,"services.html")

def terms(request):
    return render(request,"terms.html")

def privacy(request):
    return render(request,"privacy.html")