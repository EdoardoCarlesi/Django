import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'third_project.settings')

import django

django.setup()


import random
from app.models import User
from faker import Faker


fakegen = Faker()


def populate(N=5):
    
    for entry in range(N):

        # Create fake data for one entry
        name = fakegen.name().split(' ')
        fake_name, fake_surname = name[0], name[1]
        fake_email = fakegen.email()

        # Create a user entry
        user = User.objects.get_or_create(first_name=fake_name, last_name=fake_surname, email=fake_email)[0]

if __name__ == '__main__':

    print('Populating!')
    populate(N=100)
    print('Done')
