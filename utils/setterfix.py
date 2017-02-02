
import sys
import os
import django 
import csv


path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'coop')

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE']='coop.settings'

# this must be invoked in external scripts that 
# want to access the django app classes
django.setup()

from members.models import User,Member
from guide.models import ArtificialProblem

def find_member_by_full_name(full_name):
    for m in Member.objects.all():
        if m.__str__()==full_name:
            return m

    return False

def set_owners():
    c = 0
    adm = Member.objects.get(user__first_name='admin')
    for p in ArtificialProblem.objects.all():
        if find_member_by_full_name(p.setter):
            p.owner = find_member_by_full_name(p.setter)
            p.save()

            c+=1
        else:
            p.owner = adm
            p.save()

    return c


def count_matches():
    c = 0
    for p in ArtificialProblem.objects.all():
        if find_member_by_full_name(p.setter):

            c+=1

    return c



def count_mismatches():
    c = 0
    for p in ArtificialProblem.objects.all():
        if find_member_by_full_name(p.setter)==False and p.setter!='unknown'and p.setter!='Unknown' and p.setter!='':
            print("{} {}".format(p.id,p.setter))
            c+=1

    return c


