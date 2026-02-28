from django.core.management import BaseCommand


class Command(BaseCommand):
    help="Prints Hello World"

    def handle(self, *args, **kwargs):
        # we write the logic

        self.stdout.write("Hello World")
