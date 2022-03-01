from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):
    """ Command Create/Delete house rules """

    help = 'This Command create or delete house rules'

    def add_arguments(self, parser):
        parser.add_argument(
            '--create',
            action='store_true',
            help='Create house rules'
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete house rules'
        )

    def handle(self, *args, **options):
        house_rules = [
            "No smoking.",
            "No parties or events",
            "No pets/Pets allowed.",
            "No unregistered guests",
            "No food or drink in bedrooms",
            "No loud noise after 11 PM",
        ]
        if options['create']:
            for i in house_rules:
                if not HouseRule.objects.filter(name=i):
                    HouseRule.objects.create(name=i)
            self.stdout.write(self.style.SUCCESS(f'{len(house_rules)} house rules created!'))

        elif options['delete']:
            HouseRule.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All house rules deleted!'))

        else:
            self.stdout.write(self.style.ERROR('Options are not given. (--create or --delete)'))
    