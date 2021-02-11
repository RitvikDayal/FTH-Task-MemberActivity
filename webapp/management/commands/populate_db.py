from datetime import timedelta, datetime
import names
import pytz
from random import randint, choice, random
from webapp.models import Member, Activity
from django.core.management.base import BaseCommand

def gen_datetime(min_year=2020, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random()

class Command(BaseCommand):
    help = 'Populating Data base with random users and activity log.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
    
    def handle(self, *args, **kwargs):
        total = kwargs['total']
        
        for i in range(total):
            
            member = Member.objects.create(
                        real_name=names.get_full_name(),
                        tz=choice(pytz.all_timezones),
                    )

            Activity.objects.create(
                member=member, 
                start_time=gen_datetime().strftime("%Y-%m-%d %H:%M:%S"),
                end_time=gen_datetime().strftime("%Y-%m-%d %H:%M:%S")
            )