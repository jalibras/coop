
from django.db import models


class PermissionMixin(object):

# this is a class method because we create instances of a class 
    @classmethod
    def can_create(cls,user):
        return True

# OTOH it is conceivable that we have an instance already created and
# we need to check if the user can save that particular instance to the db
# something like
# if user.groups intersection object.add_groups is not empty 
# then return True
    def can_save(self,user):
        return True

    def can_read(self,user):
        return True

    def can_update(self,user):
        return True

    def can_delete(self,user):
        return True


