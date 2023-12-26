from django.contrib import admin

# Register your models here.
from .models import Topik, Entry

admin.site.register(Topik)
admin.site.register(Entry)
