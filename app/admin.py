from django.contrib import admin
from app.models import Person, Category, Division, Dismissed

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Division)
admin.site.register(Dismissed)
