# Intro

An online bouldering guidebook for the Galway climbing coop. For the moment 
it is hosted at http://galwayclimbing.pythonanywhere.com


# Installation


requires python 3.4, Django 1.10, Django Rest Framework, django-filter, Crispy-forms, Boostrap 3.3. jquery, imagemapster

Clone the repo and 
then run 

$ cd coop/coop

$ python manage.py runserver 

This will serve the site on localhost:8000

# TODO list

1. Password recovery (DONE)

2. Implement searching and filtering on the problem list page. 
Users should be able to filter problems by a single grade and 
possibly by a range eg find all problems in the range 6A-6C 

3. Make the coop problem list the default homepage. (DONE)

4. Add a member profile page, photos, links, etc

5. Implement a problem ticklist for members (DONE)

6. Implement problem upload for members (DONE)

7. Add problem edit page for owners
