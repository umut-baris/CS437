import json

from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST', 'GET'])
def api_home(request, *args, **kwargs):
    '''
    data = {}
    instance = CustomerSensitiveData.objects.all().order_by("?").first()
    if instance:
        #data = model_to_dict(model_data) #unsafe version
        #data = model_to_dict(model_data, fields= ['name', 'surname']) #safe version
        data = CustomerSensitiveDataSerializer(instance).data
    return JsonResponse(data, safe= False)
    '''

        