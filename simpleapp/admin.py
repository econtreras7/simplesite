from pyexpat import model
from django.contrib import admin

from simpleapp.models import Business

# Register your models here.


class BusinessInLine(admin.TabularInline):
    model = Business
    
class BusinessAdmin(admin.ModelAdmin):
    inlines =[
        BusinessInLine
    ]
#errors when i try to register below....
admin.site.register(Business)