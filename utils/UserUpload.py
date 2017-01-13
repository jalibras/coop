
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

def import_user(first_name,last_name,email,update_existing=False,import_as_members=True):
    try:
        u = User.objects.get(email=email)
        if update_existing:
            u.first_name=first_name
            u.last_name=last_name
            u.email=email
            u.save()
            if import_as_members and hasattr(u,'member')==False:
                m = Member()
                m.user = u
                m.save()
            return (True, 'Updated existing user with email {em}'.format(em=email))
        else:
            return (False, 'User with email{em} already exists'.format(em=email))
    except:
        u = User.objects.create_user(email,email)
        u.first_name=first_name
        u.last_name=last_name
        u.save()
        if import_as_members:
            m = Member()
            m.user = u
            m.save()
        return (True, 'Created new user with email {em}'.format(em=email))



# look for the -f flag
if '-f' in sys.argv:
    filename = sys.argv[sys.argv.index('-f')+1]
    print("importing from {fn}".format(fn=filename))
    with open(filename,newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        try:
            first_name_index = header_row.index('First Name')
        except:
            raise ValueError('header row has no "First Name"')
        try:
            last_name_index = header_row.index('Last Name')
        except:
            raise ValueError('header row has no "Last Name"')
        try:
            email_index = header_row.index('Email')
        except:
            raise ValueError('header row has no "Email"')
        print(header_row)
        for row in reader:
            try:
                import_user(row[first_name_index],row[last_name_index],row[email_index],update_existing='-u' in sys.argv,import_as_members='-m' in sys.argv)
            except:
                print('failed with data {rw}'.format(rw=str(row)))
            #print(row)
            pass



