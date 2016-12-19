from django.contrib.auth.decorators import user_passes_test

def member_required(*args,**kwargs):
    test_func = lambda u:hasattr(u,'member')
    return user_passes_test(test_func,*args,**kwargs)


