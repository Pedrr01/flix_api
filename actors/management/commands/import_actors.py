from django.core.management.base import BaseCommand
from datetime import datetime
import csv
from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores'
        )
    
    def  handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['nome']
                birthday = datetime.strptime(row['nascimento'], '%Y-%m-%d').date()
                nationality = row['nacionalidade']

                self.stdout.write(self.style.NOTICE(f'Processando: {name}'))

                Actor.objects.create(
                    name = name,
                    birthday = birthday,
                    nationality = nationality,
                )
        
        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO!'))