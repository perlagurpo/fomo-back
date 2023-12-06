# myapp/management/commands/my_command.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Descripción de tu comando'

    def add_arguments(self, parser):
        parser.add_argument('fecha', type=str, help='fecha')

    def handle(self, *args, **options):
        # Lógica de tu comando aquí
        mi_parametro = options['mi_parametro']
        self.stdout.write(self.style.SUCCESS('Comando ejecutado con éxito'))
