from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    phone_number = models.CharField(unique=True, blank=True, null=True, max_length=20,
                                    error_messages={
                                        'unique': "A user with that phone number already exists."
                                    })
    mental_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                    error_messages={
                                        'max_value': "Mental score can't be greater than 100%",
                                        'min_value': "Mental score can't be less than 0%"
                                    })
    
    relative_name = models.CharField(max_length=50, blank=True, null=True)
    relative_email = models.EmailField(blank=True, null=True)
    relative_phone_number = models.CharField(blank=True, null=True, max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
    
