from django.test import TestCase

from django.utils import timezone
from guide.templatetags.problem_list import list_display
from guide.models import ArtificialProblem,ProblemImage


import random

# Create your tests here.


# testing models


class ProblemImageTest(TestCase):
    def setUp(self):
        ProblemImage.objects.create()

    def test_base_problem_pictures_method(self):
        pass



class ArtificialProblemTest(TestCase):
    def setUp(self):
        ArtificialProblem.objects.create(
                setter='unknown',
                description='test problem 1',
                holds = 'Mint',
                date = timezone.now().date()
                )
            


class ProblemImageTest(TestCase):
    def setUp(self):
        ProblemImage.objects.create(
                problem = ArtificialProblem.objects.get(description='test problem 1'),
                image_file=None
                )

    def test_base_problem_pictures_method(self):
        pass


test_artificial_problem = ArtificialProblem(
        setter='unknown',
        description='A test problem, Sit start.',
        holds = 'Mint',
        date = timezone.now().date()
        )


test_problems = [

# test to make sure that my template tag works

class ListDisplayTagTest(TestCase):
    def test_list_display_not_NONE_for_date(self):
        self.assertIsNot(list_display(test_artificial_problem,'date'),'NONE')

