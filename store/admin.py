from django.contrib import admin
from .models import Store, Book, Author
# Register your models here.
admin.site.register(Store)
admin.site.register(Book)
admin.site.register(Author)