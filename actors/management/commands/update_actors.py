from django.core.management.base import BaseCommand
from datetime import datetime
import csv
from actors.models import Actor

# Update para os campos que ficaram sem registro ou se tiver mudado os dados (nacionalidade):
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Arquivo CSV com nacionalidades atualizadas'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        atualizados = 0

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['nome']
                birthday = datetime.strptime(row['nascimento'], '%Y-%m-%d').date()
                new_nationality = row['nacionalidade'].strip()

                
                actor = Actor.objects.get(name=name, birthday=birthday)
                #Verifica se a nacionalidade atual do ator é diferente da nova nacionalidade e Verifica se não está vazia.
                if actor.nationality != new_nationality and new_nationality:
                    actor.nationality = new_nationality
                    actor.save()
                    atualizados += 1
                    self.stdout.write(self.style.SUCCESS(f'Atualizado: {name}'))
                

        self.stdout.write(self.style.SUCCESS(f'Atualizações concluídas: {atualizados}'))
    
