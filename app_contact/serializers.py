from rest_framework import serializers

from .models import Contact, Address


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
