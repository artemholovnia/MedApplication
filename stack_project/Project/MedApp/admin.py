from django.contrib import admin
from .models import *
# Register your models here.

class UslugaDlaClientaInline(admin.StackedInline):
    model = UslugaDlaClienta
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    inlines = [UslugaDlaClientaInline]

admin.site.register(Client, ClientAdmin)
admin.site.register(Usluga)
admin.site.register(Permission)