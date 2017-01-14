
import sys
import os
import django 
import csv
import datetime


path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'coop')

sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE']='coop.settings'

# this must be invoked in external scripts that 
# want to access the django app classes
django.setup()

from guide.models import BaseProblem,ArtificialProblem,NaturalProblem,Area,Sector

from members.models import Member


def date_converter(date):
    d = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12',
            }
    tmp = date.split('-')
    return datetime.date(int(tmp[2]),int(d[tmp[1]]),int(tmp[0]))


def import_artificial_problem(area_id,grade,sector_name,holds,comments,sit,date_text,owner_id=30,setter='unknown'):
    area = Area.objects.get(id=area_id)
    owner = Member.objects.get(id=owner_id)
    date=date_converter(date_text)
    try:
        sector = Sector.objects.get(name=sector_name,area=area)
    except:
        sector = Sector(area=area,name=sector_name)
        sector.save()
    description = comments
    if sit=='TRUE':
        description = 'Sit start. '+description

    a = ArtificialProblem(area=area,sector=sector,grade=grade,owner=owner,setter=setter,holds=holds,date=date,description=description)
    a.save()


def bulk_problem_import(filename, area_id):
    with open(filename,newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        grade_i,sector_name_i,holds_i,sit_i,date_i,comments_i = header_row.index('grade'),header_row.index('sector_name'),header_row.index('holds'),header_row.index('sit'),header_row.index('date'),header_row.index('comments')
        for row in reader:
            import_artificial_problem(
            #print(
                    area_id,
                    row[grade_i],
                    row[sector_name_i],
                    row[holds_i],
                    row[comments_i],
                    row[sit_i],
                    row[date_i]
                    )
                #)

