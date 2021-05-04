from django.db import models

CONTACT_TYPE_CHOICES = (
    ('private', 'Privat'),
    ('business', 'Business'),
)


class Contact(models.Model):
    name = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256, blank=True)
    type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES, default='private')

    def __str__(self):
        if 'private' in self.type:
            return '%s %s' % (self.first_name, self.name)
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return '%s, %s %s' % (self.street, self.zip, self.city)