import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yarntail_project.settings')

import django
django.setup()

from yarntail.models import *


def populate():

    add_admin()

    add_user(username="Hulk", password="marvel", email="hulkisgreen@gamma.com", first_name="Bruce", last_name="Banner", dob="1962-05-01")

    add_user(username="Wolverine", password="xmen", email="adamantium@skeleton.claws", first_name="James", last_name="Howlett", dob="1974-06-03")

    add_user(username='test', password='test', email='test@mailinator.com', first_name='Test', last_name='User', dob='1995-01-01')

    add_user(username='KingOfGondor', password='lotr', email='isildurs@bane.ring', first_name='Aragorn', last_name='Strider', dob='1990-01-01')

    add_user(username="TheGreyPilgrim", password="shadowfax", email="magic@rox.com", first_name="Gandalf", last_name="Mithrandil", dob='1957-06-07')

    add_user(username='user1', password='password', email='awesome@captains_of_the_world.com', first_name='Captain', last_name='Awesome', dob='1990-12-12')

    add_user(username='TheGardener', password='rosie', email='secrethero@ofthestory.shire', first_name='Sam-Wise', last_name='Gamgee', dob='1986-08-12')

    add_pattern(title="Pipe weed pouch", description="A usefuly puch to hold your pipe weed on those long adventures to save Middle Earth.",
                user="KingOfGondor", design="1 1 knit 011000 2 1 knit 000110 3 1 knit 010010 4 1 knit 101010 5 1 knit 001110 6 1 knit 000000 7 1 knit 000000 8 1 knit 000000 9 1 knit 000000 10 1 knit 000000 11 1 knit 000000 12 1 knit 000000 13 1 knit 000000 14 1 knit 000000 15 1 knit 000000 16 1 knit 000000 1 2 knit 000000 2 2 knit 000000 3 2 knit 000000 4 2 knit 000000 5 2 knit 000000 6 2 knit 000000 7 2 knit 000000 8 2 knit 000000 9 2 knit 000000 10 2 knit 000000 11 2 knit 000000 12 2 knit 000000 13 2 knit 000000 14 2 knit 000000 15 2 knit 000000 16 2 knit 000000 1 3 knit 000000 2 3 knit 000000 3 3 knit 000000 4 3 knit 000000 5 3 knit 000000 6 3 knit 808080 7 3 knit C91111 8 3 knit 000000 9 3 knit 000000 10 3 knit 000000 11 3 knit C91111 12 3 knit 000000 13 3 knit 000000 14 3 knit 000000 15 3 knit 000000 16 3 knit 000000 1 4 knit 000000 2 4 knit 000000 3 4 knit 000000 4 4 knit 000000 5 4 knit 808080 6 4 knit C91111 7 4 knit 000000 8 4 knit 000000 9 4 knit 000000 10 4 knit C91111 11 4 knit 808080 12 4 knit 000000 13 4 knit 000000 14 4 knit 000000 15 4 knit 000000 16 4 knit 000000 1 5 knit 000000 2 5 knit 000000 3 5 knit 000000 4 5 knit 000000 5 5 knit C91111 6 5 knit 808080 7 5 knit 000000 8 5 knit 000000 9 5 knit C91111 10 5 knit 808080 11 5 knit 000000 12 5 knit 000000 13 5 knit 000000 14 5 knit 000000 15 5 knit 000000 16 5 knit 000000 1 6 knit 000000 2 6 knit 000000 3 6 knit 000000 4 6 knit 808080 5 6 knit C91111 6 6 knit 000000 7 6 knit 000000 8 6 knit C91111 9 6 knit 808080 10 6 knit 000000 11 6 knit 000000 12 6 knit 000000 13 6 knit C91111 14 6 knit 000000 15 6 knit 000000 16 6 knit 000000 1 7 knit 000000 2 7 knit 000000 3 7 knit 808080 4 7 knit C91111 5 7 knit 000000 6 7 knit 000000 7 7 knit 808080 8 7 knit C91111 9 7 knit 000000 10 7 knit 000000 11 7 knit 000000 12 7 knit C91111 13 7 knit 808080 14 7 knit 000000 15 7 knit 000000 16 7 knit 000000 1 8 knit 000000 2 8 knit 000000 3 8 knit C91111 4 8 knit 808080 5 8 knit 000000 6 8 knit 000000 7 8 knit C91111 8 8 knit 000000 9 8 knit 000000 10 8 knit 000000 11 8 knit C91111 12 8 knit 808080 13 8 knit 000000 14 8 knit 000000 15 8 knit 000000 16 8 knit 000000 1 9 knit 000000 2 9 knit 808080 3 9 knit C91111 4 9 knit 000000 5 9 knit 000000 6 9 knit C91111 7 9 knit 808080 8 9 knit 000000 9 9 knit 000000 10 9 knit 808080 11 9 knit C91111 12 9 knit 000000 13 9 knit 000000 14 9 knit 000000 15 9 knit 000000 16 9 knit 000000 1 10 knit 000000 2 10 knit 000000 3 10 knit 808080 4 10 knit 000000 5 10 knit 808080 6 10 knit C91111 7 10 knit 000000 8 10 knit 000000 9 10 knit 000000 10 10 knit C91111 11 10 knit 000000 12 10 knit 000000 13 10 knit 000000 14 10 knit 000000 15 10 knit 000000 16 10 knit 000000 1 11 knit 000000 2 11 knit 000000 3 11 knit 000000 4 11 knit 808080 5 11 knit C91111 6 11 knit 000000 7 11 knit 000000 8 11 knit 000000 9 11 knit C91111 10 11 knit 808080 11 11 knit 000000 12 11 knit 000000 13 11 knit 000000 14 11 knit 000000 15 11 knit 000000 16 11 knit 000000 1 12 knit 000000 2 12 knit 000000 3 12 knit 808080 4 12 knit C91111 5 12 knit 000000 6 12 knit 000000 7 12 knit 000000 8 12 knit 808080 9 12 knit C91111 10 12 knit 000000 11 12 knit 000000 12 12 knit 000000 13 12 knit 000000 14 12 knit 000000 15 12 knit 000000 16 12 knit 000000 1 13 knit 000000 2 13 knit 000000 3 13 knit C91111 4 13 knit 000000 5 13 knit 000000 6 13 knit 000000 7 13 knit 000000 8 13 knit C91111 9 13 knit 000000 10 13 knit 000000 11 13 knit 000000 12 13 knit 000000 13 13 knit 000000 14 13 knit 000000 15 13 knit 000000 16 13 knit 000000 1 14 knit 000000 2 14 knit 000000 3 14 knit 000000 4 14 knit 000000 5 14 knit 000000 6 14 knit 000000 7 14 knit 808080 8 14 knit C91111 9 14 knit 000000 10 14 knit 000000 11 14 knit 000000 12 14 knit 000000 13 14 knit 000000 14 14 knit 000000 15 14 knit 000000 16 14 knit 000000 1 15 knit 000000 2 15 knit 000000 3 15 knit 000000 4 15 knit 000000 5 15 knit 000000 6 15 knit 000000 7 15 knit 000000 8 15 knit 000000 9 15 knit 000000 10 15 knit 000000 11 15 knit 000000 12 15 knit 000000 13 15 knit 000000 14 15 knit 000000 15 15 knit 000000 16 15 knit 000000 1 16 knit 000000 2 16 knit 000000 3 16 knit 000000 4 16 knit 000000 5 16 knit 000000 6 16 knit 000000 7 16 knit 000000 8 16 knit 000000 9 16 knit 000000 10 16 knit 000000 11 16 knit 000000 12 16 knit 000000 13 16 knit 000000 14 16 knit 000000 15 16 knit 000000 16 16 knit 000000 ")

    add_pattern(title='Fingerless Gloves', description='Classy fingerless gloves. Perfect for a smartphone user', user='user1',
                design="1 1 knit FFFFFF 2 1 knit FFFFFF 3 1 knit D84E09 4 1 knit FD9800 5 1 knit D84E09 6 1 knit FD9800 7 1 knit D84E09 8 1 knit FD9800 9 1 knit D84E09 10 1 knit FFFFFF 1 2 knit FFFFFF 2 2 knit FFFFFF 3 2 knit D84E09 4 2 knit FD9800 5 2 knit D84E09 6 2 knit FD9800 7 2 knit D84E09 8 2 knit FD9800 9 2 knit D84E09 10 2 knit FD9800 1 3 knit FD9800 2 3 knit FFFFFF 3 3 knit C91111 4 3 knit C91111 5 3 knit C91111 6 3 knit C91111 7 3 knit C91111 8 3 knit FD9800 9 3 knit D84E09 10 3 knit FD9800 1 4 knit FD9800 2 4 knit C91111 3 4 knit D84E09 4 4 knit D84E09 5 4 knit D84E09 6 4 knit D84E09 7 4 knit D84E09 8 4 knit C91111 9 4 knit D84E09 10 4 knit FD9800 1 5 knit FD9800 2 5 knit C91111 3 5 knit D84E09 4 5 drop FFFFFF 5 5 drop FFFFFF 6 5 drop FFFFFF 7 5 drop FFFFFF 8 5 knit D84E09 9 5 knit C91111 10 5 knit FD9800 1 6 knit FD9800 2 6 knit C91111 3 6 knit D84E09 4 6 drop FFFFFF 5 6 drop FFFFFF 6 6 drop FFFFFF 7 6 drop FFFFFF 8 6 knit D84E09 9 6 knit C91111 10 6 knit FFFFFF 1 7 knit FFFFFF 2 7 knit FD9800 3 7 knit C91111 4 7 knit FF8000 5 7 knit FF8000 6 7 knit FF8000 7 7 knit FF8000 8 7 knit D84E09 9 7 knit C91111 10 7 knit FFFFFF 1 8 knit FFFFFF 2 8 knit FFFFFF 3 8 knit 000000 4 8 knit C91111 5 8 knit C91111 6 8 knit C91111 7 8 knit C91111 8 8 knit C91111 9 8 knit FFFFFF 10 8 knit FFFFFF 1 9 knit FFFFFF 2 9 knit FFFFFF 3 9 knit 000000 4 9 knit 000000 5 9 knit 000000 6 9 knit 000000 7 9 knit 000000 8 9 knit 000000 9 9 knit FFFFFF 10 9 knit FFFFFF 1 10 knit FFFFFF 2 10 knit FFFFFF 3 10 knit 000000 4 10 knit 000000 5 10 knit 000000 6 10 knit 000000 7 10 knit 000000 8 10 knit 000000 9 10 knit FFFFFF 10 10 knit FFFFFF ")

    add_pattern(title="Claw Cleaner", description="A useful tool for cleaning the blood of your enemies off your claws.", user="Wolverine",
                design="1 1 knit 000000 2 1 knit 000000 3 1 knit 000000 4 1 knit 000000 5 1 knit 000000 6 1 knit 000000 7 1 knit 000000 8 1 knit 000000 9 1 knit 000000 10 1 knit 000000 11 1 knit 000000 12 1 knit 000000 13 1 knit 000000 14 1 knit 000000 15 1 knit 000000 16 1 knit 000000 1 2 knit 000000 2 2 knit 000000 3 2 knit 000000 4 2 knit 000000 5 2 knit 000000 6 2 knit 000000 7 2 knit 000000 8 2 knit 000000 9 2 knit 000000 10 2 knit 000000 11 2 knit 000000 12 2 knit 000000 13 2 knit 000000 14 2 knit 000000 15 2 knit 000000 16 2 knit 000000 1 3 knit 000000 2 3 knit 000000 3 3 knit 000000 4 3 knit 000000 5 3 knit 000000 6 3 knit 808080 7 3 knit C91111 8 3 knit 000000 9 3 knit 000000 10 3 knit 000000 11 3 knit C91111 12 3 knit 000000 13 3 knit 000000 14 3 knit 000000 15 3 knit 000000 16 3 knit 000000 1 4 knit 000000 2 4 knit 000000 3 4 knit 000000 4 4 knit 000000 5 4 knit 808080 6 4 knit C91111 7 4 knit 000000 8 4 knit 000000 9 4 knit 000000 10 4 knit C91111 11 4 knit 808080 12 4 knit 000000 13 4 knit 000000 14 4 knit 000000 15 4 knit 000000 16 4 knit 000000 1 5 knit 000000 2 5 knit 000000 3 5 knit 000000 4 5 knit 000000 5 5 knit C91111 6 5 knit 808080 7 5 knit 000000 8 5 knit 000000 9 5 knit C91111 10 5 knit 808080 11 5 knit 000000 12 5 knit 000000 13 5 knit 000000 14 5 knit 000000 15 5 knit 000000 16 5 knit 000000 1 6 knit 000000 2 6 knit 000000 3 6 knit 000000 4 6 knit 808080 5 6 knit C91111 6 6 knit 000000 7 6 knit 000000 8 6 knit C91111 9 6 knit 808080 10 6 knit 000000 11 6 knit 000000 12 6 knit 000000 13 6 knit C91111 14 6 knit 000000 15 6 knit 000000 16 6 knit 000000 1 7 knit 000000 2 7 knit 000000 3 7 knit 808080 4 7 knit C91111 5 7 knit 000000 6 7 knit 000000 7 7 knit 808080 8 7 knit C91111 9 7 knit 000000 10 7 knit 000000 11 7 knit 000000 12 7 knit C91111 13 7 knit 808080 14 7 knit 000000 15 7 knit 000000 16 7 knit 000000 1 8 knit 000000 2 8 knit 000000 3 8 knit C91111 4 8 knit 808080 5 8 knit 000000 6 8 knit 000000 7 8 knit C91111 8 8 knit 000000 9 8 knit 000000 10 8 knit 000000 11 8 knit C91111 12 8 knit 808080 13 8 knit 000000 14 8 knit 000000 15 8 knit 000000 16 8 knit 000000 1 9 knit 000000 2 9 knit 808080 3 9 knit C91111 4 9 knit 000000 5 9 knit 000000 6 9 knit C91111 7 9 knit 808080 8 9 knit 000000 9 9 knit 000000 10 9 knit 808080 11 9 knit C91111 12 9 knit 000000 13 9 knit 000000 14 9 knit 000000 15 9 knit 000000 16 9 knit 000000 1 10 knit 000000 2 10 knit 000000 3 10 knit 808080 4 10 knit 000000 5 10 knit 808080 6 10 knit C91111 7 10 knit 000000 8 10 knit 000000 9 10 knit 000000 10 10 knit C91111 11 10 knit 000000 12 10 knit 000000 13 10 knit 000000 14 10 knit 000000 15 10 knit 000000 16 10 knit 000000 1 11 knit 000000 2 11 knit 000000 3 11 knit 000000 4 11 knit 808080 5 11 knit C91111 6 11 knit 000000 7 11 knit 000000 8 11 knit 000000 9 11 knit C91111 10 11 knit 808080 11 11 knit 000000 12 11 knit 000000 13 11 knit 000000 14 11 knit 000000 15 11 knit 000000 16 11 knit 000000 1 12 knit 000000 2 12 knit 000000 3 12 knit 808080 4 12 knit C91111 5 12 knit 000000 6 12 knit 000000 7 12 knit 000000 8 12 knit 808080 9 12 knit C91111 10 12 knit 000000 11 12 knit 000000 12 12 knit 000000 13 12 knit 000000 14 12 knit 000000 15 12 knit 000000 16 12 knit 000000 1 13 knit 000000 2 13 knit 000000 3 13 knit C91111 4 13 knit 000000 5 13 knit 000000 6 13 knit 000000 7 13 knit 000000 8 13 knit C91111 9 13 knit 000000 10 13 knit 000000 11 13 knit 000000 12 13 knit 000000 13 13 knit 000000 14 13 knit 000000 15 13 knit 000000 16 13 knit 000000 1 14 knit 000000 2 14 knit 000000 3 14 knit 000000 4 14 knit 000000 5 14 knit 000000 6 14 knit 000000 7 14 knit 808080 8 14 knit C91111 9 14 knit 000000 10 14 knit 000000 11 14 knit 000000 12 14 knit 000000 13 14 knit 000000 14 14 knit 000000 15 14 knit 000000 16 14 knit 000000 1 15 knit 000000 2 15 knit 000000 3 15 knit 000000 4 15 knit 000000 5 15 knit 000000 6 15 knit 000000 7 15 knit 000000 8 15 knit 000000 9 15 knit 000000 10 15 knit 000000 11 15 knit 000000 12 15 knit 000000 13 15 knit 000000 14 15 knit 000000 15 15 knit 000000 16 15 knit 000000 1 16 knit 000000 2 16 knit 000000 3 16 knit 000000 4 16 knit 000000 5 16 knit 000000 6 16 knit 000000 7 16 knit 000000 8 16 knit 000000 9 16 knit 000000 10 16 knit 000000 11 16 knit 000000 12 16 knit 000000 13 16 knit 000000 14 16 knit 000000 15 16 knit 000000 16 16 knit 000000 ")

    add_pattern(title="Incredible Shorts", description="A pair of shorts that won't break when you turn into a massive green "
                                                       "rage monster. HULK SMASH!", user="Hulk", design="1 1 knit 7E44BC 2 1 purl 1C8E0D 3 1 knit 7E44BC 4 1 knit 2862B9 5 1 knit 2862B9 6 1 knit 7E44BC 7 1 purl 1C8E0D 8 1 knit 7E44BC 9 1 knit 2862B9 10 1 knit 2862B9 11 1 knit 2862B9 12 1 knit 7E44BC 13 1 purl 1C8E0D 14 1 knit 7E44BC 15 1 knit 2862B9 16 1 knit 2862B9 1 2 knit 7E44BC 2 2 purl 1C8E0D 3 2 knit 7E44BC 4 2 knit 2862B9 5 2 knit 2862B9 6 2 knit 7E44BC 7 2 purl 1C8E0D 8 2 knit 7E44BC 9 2 knit 2862B9 10 2 knit 2862B9 11 2 knit 7E44BC 12 2 purl 1C8E0D 13 2 knit 7E44BC 14 2 knit 2862B9 15 2 knit 2862B9 16 2 knit 2862B9 1 3 knit 7E44BC 2 3 purl 1C8E0D 3 3 knit 7E44BC 4 3 knit 2862B9 5 3 knit 2862B9 6 3 knit 7E44BC 7 3 purl 1C8E0D 8 3 knit 7E44BC 9 3 knit 2862B9 10 3 knit 2862B9 11 3 knit 7E44BC 12 3 purl 1C8E0D 13 3 knit 7E44BC 14 3 knit 2862B9 15 3 knit 2862B9 16 3 knit 7E44BC 1 4 purl 1C8E0D 2 4 knit 7E44BC 3 4 knit 2862B9 4 4 knit 2862B9 5 4 knit 2862B9 6 4 knit 7E44BC 7 4 purl 1C8E0D 8 4 knit 7E44BC 9 4 knit 2862B9 10 4 knit 2862B9 11 4 knit 7E44BC 12 4 purl 1C8E0D 13 4 knit 7E44BC 14 4 knit 2862B9 15 4 knit 2862B9 16 4 knit 7E44BC 1 5 purl 1C8E0D 2 5 knit 7E44BC 3 5 knit 2862B9 4 5 knit 2862B9 5 5 knit 7E44BC 6 5 purl 1C8E0D 7 5 knit 7E44BC 8 5 knit 2862B9 9 5 knit 2862B9 10 5 knit 2862B9 11 5 knit 7E44BC 12 5 purl 1C8E0D 13 5 knit 7E44BC 14 5 knit 2862B9 15 5 knit 2862B9 16 5 knit 7E44BC 1 6 purl 1C8E0D 2 6 knit 7E44BC 3 6 knit 2862B9 4 6 knit 2862B9 5 6 knit 7E44BC 6 6 purl 1C8E0D 7 6 knit 7E44BC 8 6 knit 2862B9 9 6 knit 2862B9 10 6 knit 7E44BC 11 6 purl 1C8E0D 12 6 knit 7E44BC 13 6 knit 2862B9 14 6 knit 2862B9 15 6 knit 2862B9 16 6 knit 7E44BC 1 7 purl 1C8E0D 2 7 knit 7E44BC 3 7 knit 2862B9 4 7 knit 2862B9 5 7 knit 7E44BC 6 7 purl 1C8E0D 7 7 knit 7E44BC 8 7 knit 2862B9 9 7 knit 2862B9 10 7 knit 7E44BC 11 7 purl 1C8E0D 12 7 knit 7E44BC 13 7 knit 2862B9 14 7 knit 2862B9 15 7 knit 7E44BC 16 7 purl 1C8E0D 1 8 knit 7E44BC 2 8 knit 2862B9 3 8 knit 2862B9 4 8 knit 2862B9 5 8 knit 7E44BC 6 8 purl 1C8E0D 7 8 knit 7E44BC 8 8 knit 2862B9 9 8 knit 2862B9 10 8 knit 7E44BC 11 8 purl 1C8E0D 12 8 knit 7E44BC 13 8 knit 2862B9 14 8 knit 2862B9 15 8 knit 7E44BC 16 8 purl 1C8E0D 1 9 knit 7E44BC 2 9 knit 2862B9 3 9 knit 2862B9 4 9 knit 7E44BC 5 9 purl 1C8E0D 6 9 knit 7E44BC 7 9 knit 2862B9 8 9 knit 2862B9 9 9 knit 2862B9 10 9 knit 7E44BC 11 9 purl 1C8E0D 12 9 knit 7E44BC 13 9 knit 2862B9 14 9 knit 2862B9 15 9 knit 7E44BC 16 9 purl 1C8E0D 1 10 knit 7E44BC 2 10 knit 2862B9 3 10 knit 2862B9 4 10 knit 7E44BC 5 10 purl 1C8E0D 6 10 knit 7E44BC 7 10 knit 2862B9 8 10 knit 2862B9 9 10 knit 7E44BC 10 10 purl 1C8E0D 11 10 knit 7E44BC 12 10 knit 2862B9 13 10 knit 2862B9 14 10 knit 2862B9 15 10 knit 7E44BC 16 10 purl 1C8E0D 1 11 knit 7E44BC 2 11 knit 2862B9 3 11 knit 2862B9 4 11 knit 7E44BC 5 11 purl 1C8E0D 6 11 knit 7E44BC 7 11 knit 2862B9 8 11 knit 2862B9 9 11 knit 7E44BC 10 11 purl 1C8E0D 11 11 knit 7E44BC 12 11 knit 2862B9 13 11 knit 2862B9 14 11 knit 7E44BC 15 11 purl 1C8E0D 16 11 knit 7E44BC 1 12 knit 2862B9 2 12 knit 2862B9 3 12 knit 2862B9 4 12 knit 7E44BC 5 12 purl 1C8E0D 6 12 knit 7E44BC 7 12 knit 2862B9 8 12 knit 2862B9 9 12 knit 7E44BC 10 12 purl 1C8E0D 11 12 knit 7E44BC 12 12 knit 2862B9 13 12 knit 2862B9 14 12 knit 7E44BC 15 12 purl 1C8E0D 16 12 knit 7E44BC 1 13 knit 2862B9 2 13 knit 2862B9 3 13 knit 7E44BC 4 13 purl 1C8E0D 5 13 knit 7E44BC 6 13 knit 2862B9 7 13 knit 2862B9 8 13 knit 2862B9 9 13 knit 7E44BC 10 13 purl 1C8E0D 11 13 knit 7E44BC 12 13 knit 2862B9 13 13 knit 2862B9 14 13 knit 7E44BC 15 13 purl 1C8E0D 16 13 knit 7E44BC 1 14 knit 2862B9 2 14 knit 2862B9 3 14 knit 7E44BC 4 14 purl 1C8E0D 5 14 knit 7E44BC 6 14 knit 2862B9 7 14 knit 2862B9 8 14 knit 7E44BC 9 14 purl 1C8E0D 10 14 knit 7E44BC 11 14 knit 2862B9 12 14 knit 2862B9 13 14 knit 2862B9 14 14 knit 7E44BC 15 14 purl 1C8E0D 16 14 knit 7E44BC 1 15 knit 2862B9 2 15 knit 2862B9 3 15 knit 7E44BC 4 15 purl 1C8E0D 5 15 knit 7E44BC 6 15 knit 2862B9 7 15 knit 2862B9 8 15 knit 7E44BC 9 15 purl 1C8E0D 10 15 knit 7E44BC 11 15 knit 2862B9 12 15 knit 2862B9 13 15 knit 7E44BC 14 15 purl 1C8E0D 15 15 knit 7E44BC 16 15 knit 2862B9 1 16 knit 2862B9 2 16 knit 2862B9 3 16 knit 7E44BC 4 16 purl 1C8E0D 5 16 knit 7E44BC 6 16 knit 2862B9 7 16 knit 2862B9 8 16 knit 7E44BC 9 16 purl 1C8E0D 10 16 knit 7E44BC 11 16 knit 2862B9 12 16 knit 2862B9 13 16 knit 7E44BC 14 16 purl 1C8E0D 15 16 knit 7E44BC 16 16 knit 2862B9 ")

    add_pattern(title="testPattern", description="This is a pattern for test purposes.", user="test",
                design="1 1 knit FFFFFF 2 1 knit FFFFFF 3 1 knit FFFFFF 4 1 knit FFFFFF 5 1 knit FFFFFF 6 1 knit FFFFFF 7 1 knit FFFFFF 8 1 knit FFFFFF 9 1 knit FFFFFF 10 1 knit FFFFFF 11 1 knit FFFFFF 12 1 knit FFFFFF 13 1 knit FFFFFF 14 1 knit FFFFFF 15 1 knit FFFFFF 16 1 knit FFFFFF 17 1 knit FFFFFF 18 1 knit FFFFFF 19 1 knit FFFFFF 20 1 knit FFFFFF 1 2 knit FFFFFF 2 2 knit FFFFFF 3 2 knit FFFFFF 4 2 knit FFFFFF 5 2 knit FFFFFF 6 2 knit FFFFFF 7 2 knit FFFFFF 8 2 knit FFFFFF 9 2 purl FFFFFF 10 2 purl FFFFFF 11 2 purl FFFFFF 12 2 purl FFFFFF 13 2 knit FFFFFF 14 2 knit FFFFFF 15 2 knit FFFFFF 16 2 knit FFFFFF 17 2 knit FFFFFF 18 2 knit FFFFFF 19 2 knit FFFFFF 20 2 knit FFFFFF 1 3 knit FFFFFF 2 3 knit FFFFFF 3 3 knit FFFFFF 4 3 knit FFFFFF 5 3 knit FFFFFF 6 3 purl FFFFFF 7 3 purl FFFFFF 8 3 purl FFFFFF 9 3 purl FFFFFF 10 3 purl FFFFFF 11 3 purl FFFFFF 12 3 purl FFFFFF 13 3 purl FFFFFF 14 3 purl FFFFFF 15 3 purl FFFFFF 16 3 knit FFFFFF 17 3 knit FFFFFF 18 3 knit FFFFFF 19 3 knit FFFFFF 20 3 knit FFFFFF 1 4 knit FFFFFF 2 4 knit FFFFFF 3 4 knit FFFFFF 4 4 knit FFFFFF 5 4 purl FFFFFF 6 4 purl FFFFFF 7 4 purl FFFFFF 8 4 purl FFFFFF 9 4 purl FFFFFF 10 4 purl FFFFFF 11 4 purl FFFFFF 12 4 purl FFFFFF 13 4 purl FFFFFF 14 4 purl FFFFFF 15 4 purl FFFFFF 16 4 purl FFFFFF 17 4 knit FFFFFF 18 4 knit FFFFFF 19 4 knit FFFFFF 20 4 knit FFFFFF 1 5 knit FFFFFF 2 5 knit FFFFFF 3 5 knit FFFFFF 4 5 purl FFFFFF 5 5 purl FFFFFF 6 5 purl FFFFFF 7 5 purl FFFFFF 8 5 purl FFFFFF 9 5 purl FFFFFF 10 5 purl FFFFFF 11 5 purl FFFFFF 12 5 purl FFFFFF 13 5 purl FFFFFF 14 5 purl FFFFFF 15 5 purl FFFFFF 16 5 purl FFFFFF 17 5 purl FFFFFF 18 5 knit FFFFFF 19 5 knit FFFFFF 20 5 knit FFFFFF 1 6 knit FFFFFF 2 6 knit FFFFFF 3 6 purl FFFFFF 4 6 purl FFFFFF 5 6 purl FFFFFF 6 6 purl FFFFFF 7 6 knit FFFFFF 8 6 purl FFFFFF 9 6 purl FFFFFF 10 6 purl FFFFFF 11 6 purl FFFFFF 12 6 purl FFFFFF 13 6 purl FFFFFF 14 6 knit FFFFFF 15 6 purl FFFFFF 16 6 purl FFFFFF 17 6 purl FFFFFF 18 6 purl FFFFFF 19 6 knit FFFFFF 20 6 knit FFFFFF 1 7 knit FFFFFF 2 7 knit FFFFFF 3 7 purl FFFFFF 4 7 purl FFFFFF 5 7 purl FFFFFF 6 7 purl FFFFFF 7 7 knit FFFFFF 8 7 knit FFFFFF 9 7 purl FFFFFF 10 7 purl FFFFFF 11 7 purl FFFFFF 12 7 purl FFFFFF 13 7 knit FFFFFF 14 7 knit FFFFFF 15 7 purl FFFFFF 16 7 purl FFFFFF 17 7 purl FFFFFF 18 7 purl FFFFFF 19 7 knit FFFFFF 20 7 knit FFFFFF 1 8 knit FFFFFF 2 8 knit FFFFFF 3 8 purl FFFFFF 4 8 purl FFFFFF 5 8 purl FFFFFF 6 8 purl FFFFFF 7 8 knit FFFFFF 8 8 knit FFFFFF 9 8 knit FFFFFF 10 8 knit FFFFFF 11 8 knit FFFFFF 12 8 knit FFFFFF 13 8 knit FFFFFF 14 8 knit FFFFFF 15 8 purl FFFFFF 16 8 purl FFFFFF 17 8 purl FFFFFF 18 8 purl FFFFFF 19 8 knit FFFFFF 20 8 knit FFFFFF 1 9 knit FFFFFF 2 9 purl FFFFFF 3 9 purl FFFFFF 4 9 purl FFFFFF 5 9 purl FFFFFF 6 9 purl FFFFFF 7 9 knit FFFFFF 8 9 knit FFFFFF 9 9 knit FFFFFF 10 9 knit FFFFFF 11 9 knit FFFFFF 12 9 knit FFFFFF 13 9 knit FFFFFF 14 9 knit FFFFFF 15 9 purl FFFFFF 16 9 purl FFFFFF 17 9 purl FFFFFF 18 9 purl FFFFFF 19 9 purl FFFFFF 20 9 knit FFFFFF 1 10 knit FFFFFF 2 10 purl FFFFFF 3 10 purl FFFFFF 4 10 purl FFFFFF 5 10 purl FFFFFF 6 10 purl FFFFFF 7 10 purl FFFFFF 8 10 knit FFFFFF 9 10 knit FFFFFF 10 10 knit FFFFFF 11 10 knit FFFFFF 12 10 knit FFFFFF 13 10 knit FFFFFF 14 10 purl FFFFFF 15 10 purl FFFFFF 16 10 purl FFFFFF 17 10 purl FFFFFF 18 10 purl FFFFFF 19 10 purl FFFFFF 20 10 knit FFFFFF 1 11 knit FFFFFF 2 11 purl FFFFFF 3 11 purl FFFFFF 4 11 purl FFFFFF 5 11 purl FFFFFF 6 11 purl FFFFFF 7 11 purl FFFFFF 8 11 purl FFFFFF 9 11 knit FFFFFF 10 11 knit FFFFFF 11 11 knit FFFFFF 12 11 knit FFFFFF 13 11 purl FFFFFF 14 11 purl FFFFFF 15 11 purl FFFFFF 16 11 purl FFFFFF 17 11 purl FFFFFF 18 11 purl FFFFFF 19 11 purl FFFFFF 20 11 knit FFFFFF 1 12 knit FFFFFF 2 12 purl FFFFFF 3 12 purl FFFFFF 4 12 purl FFFFFF 5 12 purl FFFFFF 6 12 purl FFFFFF 7 12 purl FFFFFF 8 12 purl FFFFFF 9 12 purl FFFFFF 10 12 knit FFFFFF 11 12 knit FFFFFF 12 12 purl FFFFFF 13 12 purl FFFFFF 14 12 purl FFFFFF 15 12 purl FFFFFF 16 12 purl FFFFFF 17 12 purl FFFFFF 18 12 purl FFFFFF 19 12 purl FFFFFF 20 12 knit FFFFFF 1 13 knit FFFFFF 2 13 knit FFFFFF 3 13 purl FFFFFF 4 13 purl FFFFFF 5 13 purl FFFFFF 6 13 purl FFFFFF 7 13 purl FFFFFF 8 13 purl FFFFFF 9 13 knit FFFFFF 10 13 knit FFFFFF 11 13 knit FFFFFF 12 13 knit FFFFFF 13 13 purl FFFFFF 14 13 purl FFFFFF 15 13 purl FFFFFF 16 13 purl FFFFFF 17 13 purl FFFFFF 18 13 purl FFFFFF 19 13 knit FFFFFF 20 13 knit FFFFFF 1 14 knit FFFFFF 2 14 knit FFFFFF 3 14 purl FFFFFF 4 14 purl FFFFFF 5 14 knit FFFFFF 6 14 knit FFFFFF 7 14 purl FFFFFF 8 14 purl FFFFFF 9 14 knit FFFFFF 10 14 knit FFFFFF 11 14 knit FFFFFF 12 14 knit FFFFFF 13 14 purl FFFFFF 14 14 purl FFFFFF 15 14 purl FFFFFF 16 14 purl FFFFFF 17 14 purl FFFFFF 18 14 purl FFFFFF 19 14 knit FFFFFF 20 14 knit FFFFFF 1 15 knit FFFFFF 2 15 knit FFFFFF 3 15 purl FFFFFF 4 15 purl FFFFFF 5 15 purl FFFFFF 6 15 knit FFFFFF 7 15 knit FFFFFF 8 15 knit FFFFFF 9 15 knit FFFFFF 10 15 knit FFFFFF 11 15 knit FFFFFF 12 15 knit FFFFFF 13 15 purl FFFFFF 14 15 purl FFFFFF 15 15 purl FFFFFF 16 15 purl FFFFFF 17 15 purl FFFFFF 18 15 purl FFFFFF 19 15 knit FFFFFF 20 15 knit FFFFFF 1 16 knit FFFFFF 2 16 knit FFFFFF 3 16 knit FFFFFF 4 16 purl FFFFFF 5 16 purl FFFFFF 6 16 purl FFFFFF 7 16 purl FFFFFF 8 16 knit FFFFFF 9 16 knit FFFFFF 10 16 knit FFFFFF 11 16 knit FFFFFF 12 16 knit FFFFFF 13 16 purl FFFFFF 14 16 purl FFFFFF 15 16 purl FFFFFF 16 16 purl FFFFFF 17 16 purl FFFFFF 18 16 knit FFFFFF 19 16 knit FFFFFF 20 16 knit FFFFFF 1 17 knit FFFFFF 2 17 knit FFFFFF 3 17 knit FFFFFF 4 17 knit FFFFFF 5 17 purl FFFFFF 6 17 purl FFFFFF 7 17 purl FFFFFF 8 17 purl FFFFFF 9 17 knit FFFFFF 10 17 knit FFFFFF 11 17 knit FFFFFF 12 17 knit FFFFFF 13 17 purl FFFFFF 14 17 purl FFFFFF 15 17 purl FFFFFF 16 17 purl FFFFFF 17 17 knit FFFFFF 18 17 knit FFFFFF 19 17 knit FFFFFF 20 17 knit FFFFFF 1 18 knit FFFFFF 2 18 knit FFFFFF 3 18 knit FFFFFF 4 18 knit FFFFFF 5 18 knit FFFFFF 6 18 purl FFFFFF 7 18 purl FFFFFF 8 18 purl FFFFFF 9 18 knit FFFFFF 10 18 knit FFFFFF 11 18 knit FFFFFF 12 18 knit FFFFFF 13 18 purl FFFFFF 14 18 purl FFFFFF 15 18 purl FFFFFF 16 18 knit FFFFFF 17 18 knit FFFFFF 18 18 knit FFFFFF 19 18 knit FFFFFF 20 18 knit FFFFFF 1 19 knit FFFFFF 2 19 knit FFFFFF 3 19 knit FFFFFF 4 19 knit FFFFFF 5 19 knit FFFFFF 6 19 knit FFFFFF 7 19 knit FFFFFF 8 19 knit FFFFFF 9 19 knit FFFFFF 10 19 knit FFFFFF 11 19 knit FFFFFF 12 19 knit FFFFFF 13 19 knit FFFFFF 14 19 knit FFFFFF 15 19 knit FFFFFF 16 19 knit FFFFFF 17 19 knit FFFFFF 18 19 knit FFFFFF 19 19 knit FFFFFF 20 19 knit FFFFFF 1 20 knit FFFFFF 2 20 knit FFFFFF 3 20 knit FFFFFF 4 20 knit FFFFFF 5 20 knit FFFFFF 6 20 knit FFFFFF 7 20 knit FFFFFF 8 20 knit FFFFFF 9 20 knit FFFFFF 10 20 knit FFFFFF 11 20 knit FFFFFF 12 20 knit FFFFFF 13 20 knit FFFFFF 14 20 knit FFFFFF 15 20 knit FFFFFF 16 20 knit FFFFFF 17 20 knit FFFFFF 18 20 knit FFFFFF 19 20 knit FFFFFF 20 20 knit FFFFFF ")

    add_pattern(title='Hobbit Sweater', description='A sweater perfect for a hobbit!', user='TheGreyPilgrim',
                design="1 1 knit 000000 2 1 knit 000000 3 1 knit 000000 4 1 knit 000000 5 1 knit 000000 6 1 knit 000000 7 1 knit 000000 8 1 knit 000000 9 1 knit 000000 10 1 knit 000000 11 1 knit 000000 12 1 knit 000000 13 1 knit 000000 14 1 knit 000000 15 1 knit 000000 16 1 knit 000000 1 2 knit 000000 2 2 knit 000000 3 2 knit 000000 4 2 knit 000000 5 2 knit 000000 6 2 knit 000000 7 2 knit 000000 8 2 knit 000000 9 2 knit 000000 10 2 knit 000000 11 2 knit 000000 12 2 knit 000000 13 2 knit 000000 14 2 knit 000000 15 2 knit 000000 16 2 knit 000000 1 3 knit 000000 2 3 knit 000000 3 3 knit 000000 4 3 knit 000000 5 3 knit 000000 6 3 knit 808080 7 3 knit C91111 8 3 knit 000000 9 3 knit 000000 10 3 knit 000000 11 3 knit C91111 12 3 knit 000000 13 3 knit 000000 14 3 knit 000000 15 3 knit 000000 16 3 knit 000000 1 4 knit 000000 2 4 knit 000000 3 4 knit 000000 4 4 knit 000000 5 4 knit 808080 6 4 knit C91111 7 4 knit 000000 8 4 knit 000000 9 4 knit 000000 10 4 knit C91111 11 4 knit 808080 12 4 knit 000000 13 4 knit 000000 14 4 knit 000000 15 4 knit 000000 16 4 knit 000000 1 5 knit 000000 2 5 knit 000000 3 5 knit 000000 4 5 knit 000000 5 5 knit C91111 6 5 knit 808080 7 5 knit 000000 8 5 knit 000000 9 5 knit C91111 10 5 knit 808080 11 5 knit 000000 12 5 knit 000000 13 5 knit 000000 14 5 knit 000000 15 5 knit 000000 16 5 knit 000000 1 6 knit 000000 2 6 knit 000000 3 6 knit 000000 4 6 knit 808080 5 6 knit C91111 6 6 knit 000000 7 6 knit 000000 8 6 knit C91111 9 6 knit 808080 10 6 knit 000000 11 6 knit 000000 12 6 knit 000000 13 6 knit C91111 14 6 knit 000000 15 6 knit 000000 16 6 knit 000000 1 7 knit 000000 2 7 knit 000000 3 7 knit 808080 4 7 knit C91111 5 7 knit 000000 6 7 knit 000000 7 7 knit 808080 8 7 knit C91111 9 7 knit 000000 10 7 knit 000000 11 7 knit 000000 12 7 knit C91111 13 7 knit 808080 14 7 knit 000000 15 7 knit 000000 16 7 knit 000000 1 8 knit 000000 2 8 knit 000000 3 8 knit C91111 4 8 knit 808080 5 8 knit 000000 6 8 knit 000000 7 8 knit C91111 8 8 knit 000000 9 8 knit 000000 10 8 knit 000000 11 8 knit C91111 12 8 knit 808080 13 8 knit 000000 14 8 knit 000000 15 8 knit 000000 16 8 knit 000000 1 9 knit 000000 2 9 knit 808080 3 9 knit C91111 4 9 knit 000000 5 9 knit 000000 6 9 knit C91111 7 9 knit 808080 8 9 knit 000000 9 9 knit 000000 10 9 knit 808080 11 9 knit C91111 12 9 knit 000000 13 9 knit 000000 14 9 knit 000000 15 9 knit 000000 16 9 knit 000000 1 10 knit 000000 2 10 knit 000000 3 10 knit 808080 4 10 knit 000000 5 10 knit 808080 6 10 knit C91111 7 10 knit 000000 8 10 knit 000000 9 10 knit 000000 10 10 knit C91111 11 10 knit 000000 12 10 knit 000000 13 10 knit 000000 14 10 knit 000000 15 10 knit 000000 16 10 knit 000000 1 11 knit 000000 2 11 knit 000000 3 11 knit 000000 4 11 knit 808080 5 11 knit C91111 6 11 knit 000000 7 11 knit 000000 8 11 knit 000000 9 11 knit C91111 10 11 knit 808080 11 11 knit 000000 12 11 knit 000000 13 11 knit 000000 14 11 knit 000000 15 11 knit 000000 16 11 knit 000000 1 12 knit 000000 2 12 knit 000000 3 12 knit 808080 4 12 knit C91111 5 12 knit 000000 6 12 knit 000000 7 12 knit 000000 8 12 knit 808080 9 12 knit C91111 10 12 knit 000000 11 12 knit 000000 12 12 knit 000000 13 12 knit 000000 14 12 knit 000000 15 12 knit 000000 16 12 knit 000000 1 13 knit 000000 2 13 knit 000000 3 13 knit C91111 4 13 knit 000000 5 13 knit 000000 6 13 knit 000000 7 13 knit 000000 8 13 knit C91111 9 13 knit 000000 10 13 knit 000000 11 13 knit 000000 12 13 knit 000000 13 13 knit 000000 14 13 knit 000000 15 13 knit 000000 16 13 knit 000000 1 14 knit 000000 2 14 knit 000000 3 14 knit 000000 4 14 knit 000000 5 14 knit 000000 6 14 knit 000000 7 14 knit 808080 8 14 knit C91111 9 14 knit 000000 10 14 knit 000000 11 14 knit 000000 12 14 knit 000000 13 14 knit 000000 14 14 knit 000000 15 14 knit 000000 16 14 knit 000000 1 15 knit 000000 2 15 knit 000000 3 15 knit 000000 4 15 knit 000000 5 15 knit 000000 6 15 knit 000000 7 15 knit 000000 8 15 knit 000000 9 15 knit 000000 10 15 knit 000000 11 15 knit 000000 12 15 knit 000000 13 15 knit 000000 14 15 knit 000000 15 15 knit 000000 16 15 knit 000000 1 16 knit 000000 2 16 knit 000000 3 16 knit 000000 4 16 knit 000000 5 16 knit 000000 6 16 knit 000000 7 16 knit 000000 8 16 knit 000000 9 16 knit 000000 10 16 knit 000000 11 16 knit 000000 12 16 knit 000000 13 16 knit 000000 14 16 knit 000000 15 16 knit 000000 16 16 knit 000000 ")

    add_comment(user='TheGardener', pattern_slug='hobbit-sweater', comment="Perfect! Will knit the whole family a sweater each for the coming winter,"
                                                                           " mind you, I didn't have a sweater in Mordor and I survived, all"
                                                                           " I needed was a bit of Shire salt.")

    add_comment(user='TheGreyPilgrim', pattern_slug='pipe-weed-pouch', comment='Knitted and used this, works perfectly. Can smoke wherever I want now.')

    add_comment(user='KingOfGondor', pattern_slug='pipe-weed-pouch', comment='Thanks Gandalf, with all your knowledge that means a lot.')

    add_comment(user='user1', pattern_slug='fingerless-gloves', comment='Tried this pattern and I loved it. I highly recommend it')

    add_comment(user="Hulk", pattern_slug="claw-cleaner", comment="Good to see you taking care of those claws, check out"
                                                                  "my Incredible Shorts pattern, may be useful in your fights. "
                                                                  "May no foe stand before you!")

    add_comment(user="Hulk", pattern_slug='incredible-shorts', comment="These shorts are made for stretching, and that's just what they'll do, and"
                                                                       " one of these days these shorts will stretch all over you.")

    add_comment(user="Wolverine", pattern_slug="claw-cleaner", comment="Thanks Hulk, got to keep in top condition. I'll check it out now.")

    add_comment(user="Wolverine", pattern_slug="incredible-shorts", comment="These look really useful, going to start making them right away!")

    add_comment(user="Wolverine", pattern_slug="incredible-shorts", comment="Just test these bad boys out in a fight...no rips!"
                                                                            "Will use these from now on.")

    add_comment(user="Hulk", pattern_slug="incredible-shorts", comment="Glad you liked them Wolverine :)")

def add_user(username, password, first_name, last_name, email, dob):
    user = User.objects.create_user(username, email, password)
    user.save()

    prof = UserProfile.objects.get_or_create(user=user, first_name=first_name, last_name=last_name, date_of_birth=dob)
    return prof

def add_admin():
    user = User.objects.create_user('admin', '2087521d@student.gla.ac.uk', 'password')
    user.is_staff = True
    user.is_superuser = True
    user.save()

def add_pattern(title, description, user, design="empty pattern"):
    pattern = Pattern.objects.create(title=title, description=description, user=User.objects.get(username=user), design=design)
    return pattern

def add_comment(user, pattern_slug, comment):
    comment = Comment.objects.create(user=User.objects.get(username=user), pattern=Pattern.objects.get(slug=pattern_slug), comment_string=comment)
    return comment

# Start execution here!
if __name__ == '__main__':
    print "Starting YarnTail population script..."
    populate()
    print "Population script executed successfully"
