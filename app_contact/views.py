from rest_framework import viewsets

from .models import Contact, Address
from .serializers import ContactSerializer, AddressSerializer


class ContactApiView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class AddressApiView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
