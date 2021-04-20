from rest_framework import generics
from .serializers import PersonalDataDetailSerializer, PersonalDataViewSerializer
from .models import PersonalData


# Create your views here.
class PersonalDataCreateView(generics.CreateAPIView):
    serializer_class = PersonalDataDetailSerializer


class PersonalDataView(generics.ListAPIView):
    serializer_class = PersonalDataViewSerializer
    queryset = PersonalData.objects.all()


class PersonalDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonalDataDetailSerializer
    queryset = PersonalData.objects.all()
