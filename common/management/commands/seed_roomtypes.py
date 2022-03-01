from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):
    """ Command Create/Delete room types """

    help = 'This Command create or delete room types'

    def add_arguments(self, parser):
        parser.add_argument(
            '--create',
            action='store_true',
            help='Create room types'
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete room types'
        )


    def handle(self, *args, **options):
        room_types = [
            "Shared rooms",
            "Private rooms",
            "Entire homes/apartments",
        ]
        if options['create']:
            for i in room_types:
                if not RoomType.objects.filter(name=i):
                    RoomType.objects.create(name=i)
            self.stdout.write(self.style.SUCCESS(f'{len(room_types)} room types created!'))

        elif options['delete']:
            RoomType.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All room types deleted!'))

        else:
            self.stdout.write(self.style.ERROR('Options are not given. (--create or --delete)'))
    