from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('honor/', views.honor, name='honor'),
    path('publication/', views.publication, name='publication'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_details, name='blog_details'),
    path('organizations/', views.organization, name='organizations'),
    path('research/', views.research, name='research'),
]