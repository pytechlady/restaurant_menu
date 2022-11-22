"""
Django command to wait for the database to be ready.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database to be ready"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write('Database not up, waiting...')
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS('Database up and running!'))