import names
from django.core.management import BaseCommand

from api.models import Agent


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("num_agents", type=int, help="No. of agents")

    def handle(self, *args, **options):
        for i in range(options['num_agents']):
            Agent.objects.create(name=names.get_full_name())
