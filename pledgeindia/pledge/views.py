from django.shortcuts import render
from django.http import JsonResponse
import * from utils
# Create your views here.

def JsonData(request):
    datajson=PledgeData()
    return JsonResponse(datajson, safe=False)
