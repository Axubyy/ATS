from django.shortcuts import render


def index(request):
    return render(request, "portfolio/index.html")


def works(request):
    return render(request, "portfolio/works.html")


def contact(request):
    return render(request, "portfolio/contact.html")


def about(request):
    return render(request, "portfolio/about.html")


def components(request):
    return render(request, "portfolio/components.html")
