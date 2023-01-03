from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from django.views import generic
from .models import UserProfile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
#from customers.permissions import CanSeeProfile
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse

'''
class CustomerDetailAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #lookup_field = 'pk'

class CustomerListAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #lookup_field = 'pk'
'''
'''
class CustomerProfileAPIView(generic.):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Customer, pk=kwargs['user_id'])
        customer_serializer = CustomerSerializer(user)
        return Response(customer_serializer.data)
'''
'''
@api_view(['GET', 'POST'])
def customer_profile_view(request, pk = None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Customer, pk = pk)
            data = CustomerSerializer(obj, many = False).data
            return Response()


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    def perform_create(self, serializer):
        #serializer.save(user=self, request.user)
        print(serializer.validated_data)
        serializer.save()
''''''
@api_view(['GET', 'POST'])
def customer_alt_view(request, pk=None, *args, **kwargs):
    #permission_classes = [CanSeeProfile]
    method = request.method
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Customer, pk = pk)
            data = CustomerSerializer(obj, many = False).data
            return Response()

        queryset = Customer.objects.all()
        data = CustomerSerializer(queryset, many = True).data
        return Response(data)
    if method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.isvalid(raise_exception = True):
            print(serializer.data)
            return Response(serializer.data)
        return Response({"Invalid": "not good data"},status = 400)

    class CustomerUpdateAPIView(generics.UpdateAPIView):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
        lookup_field = 'pk'
        def perform_update(self, serializer):
            instance = serializer.save()
'''

class ProfileView(generics.RetrieveAPIView):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile = ProfileSerializer(profile).data
        return JsonResponse(profile)
        '''
        if instance:
            # data = model_to_dict(model_data) #unsafe version
            # data = model_to_dict(model_data, fields= ['name', 'surname']) #safe version
            data = ProfileSerializer(instance).data
            return JsonResponse(data['name'], safe= False)
        #profiledata = ProfileSerializer(data= request.data)
        '''
