from django.contrib import admin


from .models import BookShop, Book, BookTags, BookAuthor, BookImage

admin.site.register(BookTags)
admin.site.register(BookAuthor)
admin.site.register(BookImage)
admin.site.register(BookShop)
admin.site.register(Book)
