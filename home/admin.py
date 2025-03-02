from django.contrib import admin
from .models import About, Honor, Publication, Contact, Blog, Research, Organization_involved

admin.site.site_header = "Sujan Admin Dashboard"  # Header on the admin login page and top of each admin page
admin.site.site_title = "Sujan Admin Portal"  # Title of the admin site in browser tab
admin.site.index_title = "Welcome to Sujan's Admin Portal"  # Title on the admin index page

# Register your models here.
admin.site.register(About)
admin.site.register(Honor)
admin.site.register(Publication)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Research)
admin.site.register(Organization_involved)

