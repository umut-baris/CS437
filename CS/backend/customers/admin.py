from django.contrib import admin

# Register your models here.
from .models import UserProfile
#from .models import Profile

admin.site.register(UserProfile)