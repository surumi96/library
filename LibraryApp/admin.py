from django.contrib import admin
from . import models
from .models import Book
from .models import Order

# Register your models here.
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(models.User)
