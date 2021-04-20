from django.urls import path
from .views import *

from django.views.generic import RedirectView

urlpatterns = [
    path('test_1/', PersonalDataCreateView.as_view()),
    path('test_2/', PersonalDataView.as_view()),
    path('test_3/<int:pk>/', PersonalDataDetailView.as_view()),
]
