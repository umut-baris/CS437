from django.urls import path
from . import views

urlpatterns = [
    #path('', views.CustomerListCreateAPIView.as_view()),
    #path('<int:pk>/', views.CustomerDetailAPIView.as_view()),

    #path('profile/', views.customer_profile_view),
    path('<int:pk>/', views.ProfileView.as_view(), name = 'profile'),
]