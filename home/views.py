from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import About, Honor, Publication, Contact, Blog, Research, Organization_involved

# Create your views here.
def home(request):
    blogs = Blog.objects.filter(is_featured=True)
    Publications = Publication.objects.all()
    research = Research.objects.all()
    organizations = Organization_involved.objects.all()
    honors = Honor.objects.all()
    return render(request, 'home/home.html', {'blogs': blogs, 'Publications': Publications[:1], 'research': research[:2], 'organizations': organizations[:1], 'honors': honors[:1]})

def about(request):
    about = About.objects.all()
    return render(request, 'home/about.html', {'about': about[0]})


def honor(request):
    honor = Honor.objects.all()
    return render(request, 'home/honor.html', {'honors': honor})

def publication(request):
    publications = Publication.objects.all()
    return render(request, 'home/publication.html', {'publications': publications})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email (optional)
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['lamichhanesujan629@gmail.com','bishal.lamichhane342@gmail.com'],
        )

        # Redirect or show a success message
        return redirect('home:contact_success')  # Create a success page

    return render(request, 'home/contact.html')
    

def contact_success(request):
    return render(request, 'home/contact_success.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'home/blog.html', {'blogs': blogs})

def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    # filter all post by is_featured
    blogs = Blog.objects.filter(is_featured=True)
    return render(request, 'home/blog_details.html', {'blog': blog, 'blogs': blogs})

def research(request):
    researchs = Research.objects.all()
    blogs = Blog.objects.filter(is_featured=True)
    return render(request, 'home/research.html', {'researchs': researchs,'blogs':blogs})


def organization(request):
    organization = Organization_involved.objects.all()
    return render(request, 'home/organization.html', {'organizations': organization})