from django.contrib import admin

admin.site.site_header='Expressway | Admin'
admin.site.site_header='Expressway | Admin'
# Register your models here.
from .models import *
admin.site.register(contact)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(ordermodel)
admin.site.register(adminuser)

