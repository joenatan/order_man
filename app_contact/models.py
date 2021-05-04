from django.db import models

CONTACT_TYPE_CHOICES = (
    ('private', 'Privat'),
    ('business', 'Business'),
)


class Contact(models.Model):
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256, blank=True)
    type = models.CharField(max_length=20, default='private')


class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')