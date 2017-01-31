from django import template

import datetime

register = template.Library()

@register.filter
def list_display(value,arg):
    if hasattr(value,arg)==False:
        return "NONE"
    else:
        if isinstance(getattr(value,arg),(datetime.date,datetime.datetime)):
            return str(getattr(value,arg))
        else:
            return str(getattr(value,arg))

