import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django

django.setup()


import random
from first_app.models import AccessRecord, WebPage, Topic

from faker import Faker


fakegen = Faker()

topics = ['Gesu', 'Madonna', 'Cani', 'Maiali', 'Iddio']


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()

    return t


def populate(N=5):
    
    for entry in range(N):

        top = add_topic()
        
        # Create fake data for one entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create a WebPage entry

        webp = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        access = AccessRecord.objects.get_or_create(name=webp, date=fake_date)[0]


if __name__ == '__main__':

    print('Populating!')
    populate(N=10)
    print('Done')
