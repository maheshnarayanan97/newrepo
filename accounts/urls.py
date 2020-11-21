from django.urls import path
from .views import SignupView,UserRetrieveUpdateAPIView

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('update',UserRetrieveUpdateAPIView.as_view()), 
]
