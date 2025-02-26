from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('honor/', views.honor, name='honor'),
    path('publication/', views.publication, name='publication'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('organizations/', views.organization, name='organizations'),
    path('research/', views.research, name='research'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]