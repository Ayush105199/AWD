from django.core.management.base  import BaseCommand



#Proposed Command = python manage.py greeting Ayush
#proposed Output = Hi {name}, Good Morning
class Command(BaseCommand):

    help="Greet the User"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Specifies user name')
        

    def handle(self, *args, **kwargs):
        #write the logic
        name =kwargs['name']
        greeting= f'Hi {name},Good morning!'
        # self.stderr.write(greeting)
        # self.stdout.write(greeting)
        # self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.WARNING(greeting))