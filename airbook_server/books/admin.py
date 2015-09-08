from django.contrib import admin


from .models import BookShop, Book, BookCategory, BookAuthor, BookImage, BookShopUser

admin.site.register(BookCategory)
admin.site.register(BookAuthor)
admin.site.register(BookImage)
admin.site.register(BookShop)
admin.site.register(BookShopUser)
admin.site.register(Book)
