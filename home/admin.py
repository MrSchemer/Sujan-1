from django.contrib import admin
from .models import About, Honor, Publication, Contact, Blog, Research, Organization_involved

# Register your models here.
admin.site.register(About)
admin.site.register(Honor)
admin.site.register(Publication)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Research)
admin.site.register(Organization_involved)

