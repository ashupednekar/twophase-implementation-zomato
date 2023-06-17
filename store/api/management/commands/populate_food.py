from django.core.management import BaseCommand

from api.models import Food, Package
from faker import Faker
from faker_food import FoodProvider


fake = Faker()
fake.add_provider(FoodProvider)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("num_food", type=int, help="No. of food types")
        parser.add_argument("num_packages", type=int, help="No. of packages for each")

    def handle(self, *args, **options):
        for i in range(options['num_food']):
            food = Food.objects.create(name=fake.dish())
            for i in range(options["num_packages"]):
                Package.objects.create(food=food)
