from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Honor, Publication, Contact, Blog, Research, Organization_involved

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    about = About.objects.all()
    return render(request, 'home/about.html', {'about': about[0]})


def honor(request):
    honor = Honor.objects.all()
    return render(request, 'home/honor.html', {'honor': honor})

def publication(request):
    publication = Publication.objects.all()
    return render(request, 'home/publication.html', {'publication': publication})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'home/contact.html')
    

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'home/blog.html', {'blog': blog})

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'home/blog_details.html', {'blog': blog})

def research(request):
    research = Research.objects.all()
    return render(request, 'home/research.html', {'research': research})


def organization(request):
    organization = Organization_involved.objects.all()
    return render(request, 'home/organization.html', {'organization': organization})