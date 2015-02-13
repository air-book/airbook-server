from django.core.management.base import BaseCommand, CommandError
from books.factories import BookFactory, BookImageFactory
from books.models import Book, BookImage

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        num = int(args[0])
        Book.objects.all().delete()

        BookImage.objects.all().delete()

        for x in range(num):
            BookFactory.create()

        for book in Book.objects.all():
            BookImageFactory.create(book=book)