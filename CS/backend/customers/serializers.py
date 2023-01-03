from rest_framework import serializers
from .models import UserProfile
from . import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'name',
            'shipping_address',
            'loyalty_points',
            'payment',
            'cc_num',
            'exp',
            'cvv',
        ]