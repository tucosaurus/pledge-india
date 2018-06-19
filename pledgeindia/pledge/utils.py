from .models import *


def PledgeData():
    pledges = Pledge.objects.all()
    data = []
    for pledge in pledges:
        data.append({
            'title': pledge.title,
            'description': pledge.description
        })

    return data
