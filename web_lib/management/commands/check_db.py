from django.core.management.base import BaseCommand
from web_lib.models import Book

class Command(BaseCommand):

    help = 'Cheking DB'

    def add_arguments(self, parser):
        parser.add_argument('book_ids', help='book id', type = int, nargs='+')

    def handle(self, *args, **kwards):
        book_ids = kwards['book_ids']
        for book_id in book_ids:
            try:
                Book.objects.get(pk=1)
                self.stdout.write(self.style.SUCCESS('book with pk = "%s" exists' % book_id))
            except Book.DoesNotExist:
                self.stdout.write(self.style.ERROR('book with pk = "%s" is not found' % book_id))    