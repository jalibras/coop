from django.test import TestCase
from django.urls import reverse
from django.test import Client

from django.utils import timezone
from guide.templatetags.problem_list import list_display
from guide.models import Area,Sector,BaseProblem,ArtificialProblem,NaturalProblem,ProblemImage
from members.models import User,Member


import random

# Create your tests here.


# view tests

class ProblemViewsTest(TestCase):

    fixtures=['guide.json']
    

    def setUp(self,*args,**kwargs):
        user = User.objects.create_user('temp@gmail.com','temp@gmail.com','temp1234')
        member = Member.objects.create(user=user)
        natural_area = Area.objects.create(area_type='natural',name='test natural area')
        natural_sector = Sector.objects.create(name='test natural sector',area=natural_area)
        super(ProblemViewsTest,self).setUp(*args,**kwargs)

    def test_problem_view_returns_200_all_problems(self):
        problems = BaseProblem.objects.all()
        for p in problems:
            response = self.client.get(reverse('guide:problem', args=[p.id]))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response,'Problem')


    def test_invalid_problem_id_returns_404(self):
        c = max([p.id for p in BaseProblem.objects.all()])+1
        response = self.client.get(reverse('guide:problem', args=[c]))
        self.assertEqual(response.status_code, 404)
    
    def test_logged_in_member_has_done_toggle_button(self):
        self.client.login(username='temp@gmail.com',password='temp1234')
        prob = BaseProblem.objects.all()[0]
        response = self.client.get(reverse('guide:problem',args=[prob.id]))
        self.assertContains(response,'status-element')


    def test_artificial_problem_view_has_setter_field_but_no_firs_ascensionist(self):
        problems = ArtificialProblem.objects.all().filter(exists=True)
        test_id = problems[0].id
        response = self.client.get(reverse('guide:problem', args=[test_id]))
        self.assertContains(response,'et by')
        self.assertNotContains(response,'scensionist')



    def test_new_artificial_problem_save_works_for_logged_in_user(self):
        area= Area.objects.all().filter(area_type='artificial')[0]

        sector = Sector.objects.all().filter(area=area)[0]
        if self.client.login(username='temp@gmail.com',password='temp1234'):
            u = User.objects.get(username='temp@gmail.com')
        else:
            u = None
        new_prob_data = {
                'area':area.id,
                'grade':'6A',
                'sector':sector.id,
                'description':'A test problem with a stupid description',
                'set_by':u.member.id,
                'date':'2017-01-01',
# we need to include the following so that the image formset validates
# i don't really understand this??
                'problemimage_set-TOTAL_FORMS':'2',
                'problemimage_set-INITIAL_FORMS':'0',
                'problemimage_set-MAX_NUM_FORMS':'',
                }
        #response=self.client.get(reverse('guide:submit',args=['artificial']),new_prob_data)
        response=self.client.post(reverse('guide:submit',args=['artificial']),new_prob_data)
        self.assertEqual(response.status_code,200)
# now check that the object is in the DB
        p = ArtificialProblem.objects.get(
                description=new_prob_data['description']
                )
# check that the owner is set to the logged in user member
        self.assertEqual(p.owner,u.member)
        return


    def est_new_natural_problem_save_works_for_logged_in_user(self):
        area= Area.objects.get(name='test natural area')
        sector = Sector.objects.get(name='test natural sector')
        if self.client.login(username='temp@gmail.com',password='temp1234'):
            u = User.objects.get(username='temp@gmail.com')
        else:
            u = None
        new_prob_data = {
                'area':area.id,
                'grade':'6A',
                'sector':sector.id,
                'description':'A test natural problem with a stupid description',
                'date':'2017-01-01',
# we need to include the following so that the image formset validates
# i don't really understand this??
                'problemimage_set-TOTAL_FORMS':'2',
                'problemimage_set-INITIAL_FORMS':'0',
                'problemimage_set-MAX_NUM_FORMS':'',
                }
        response=self.client.post(reverse('guide:submit',args=['natural']),new_prob_data)
        self.assertEqual(response.status_code,200)
# now check that the object is in the DB
        p = NaturalProblem.objects.get(
                description=new_prob_data['description']
                )
# check that the owner is set to the logged in user member
        self.assertHasAttr(p,'first_ascensionist')
        self.assertEqual(p.owner,u.member)
        return




class AreaViewsTest(TestCase):

    fixtures = ['guide.json']

    def setUp(self,*args,**kwargs):
        user = User.objects.create_user('temp@gmail.com','temp@gmail.com','temp1234')
        member = Member.objects.create(user=user)
        super(AreaViewsTest,self).setUp(*args,**kwargs)

    def test_area_view_returns_200_all_areas(self):
        areas = Area.objects.all()
        for area in areas:
            response = self.client.get(reverse('guide:area_map',args=[area.id]))
            self.assertEqual(response.status_code,200)
            response = self.client.get(reverse('guide:area',args=[area.id]))
            self.assertEqual(response.status_code,200)




# testing models


