from django.core.management.base import BaseCommand
from gutendex.models import Book

class Command(BaseCommand):
    help = 'Delete all books'

    def handle(self, *args, **options):
        Book.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all books'))
