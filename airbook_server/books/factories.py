import factory
from .models import BookShop, Book, BookImage, BookShopUser
#from django.contrib.auth.models import User
from authtools.models import User
import random
import string
from django.core.files import File
import os



LOREM = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def random_string(length=10):
    return LOREM[:length]
    #return u''.join(random.choice(string.ascii_letters) for x in range(length))

def random_float(max,min):
    return random.uniform(max,min)



TEST_IMAGE = os.path.join(os.path.dirname(__file__), 'test.jpg')

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    #username = factory.LazyAttribute(lambda t: random_string(length = 20))
    email = factory.Sequence(lambda n: 'user-%s@test.com' % n, type=str)
    password = factory.PostGenerationMethodCall('set_password', 'oooo')


class BookShopUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BookShopUser
    user = factory.SubFactory(UserFactory)


class BookShopFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BookShop
    name =  factory.Sequence(lambda n: 'shop-%s' % n, type=str)#factory.LazyAttribute(lambda t: random_string())
    
    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        BookShopUserFactory.create(bookshop=self)
            
            


class BookImageFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BookImage
    image = factory.LazyAttribute(lambda t: File(open(TEST_IMAGE)))


class BookFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Book
    bookshop = factory.SubFactory(BookShopFactory)
    title = factory.LazyAttribute(lambda t: random_string(length = 40))
    description = factory.LazyAttribute(lambda t: random_string(length=200))
    #categories
    #authors
    publication_year = factory.LazyAttribute(lambda t: random.randint(1900,2014))
    price  = factory.LazyAttribute(lambda t: random.uniform(10, 100))
    editor = factory.LazyAttribute(lambda t: random_string(length=200))
    isbn_code = factory.LazyAttribute(lambda t: random_string(length=100))
    archive_code = factory.LazyAttribute(lambda t: random_string(length=10))
    conditions = factory.LazyAttribute(lambda t: random.randint(0,3))

