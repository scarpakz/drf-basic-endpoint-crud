from django.db import models
from django.contrib.auth.models import User

# USER TYPE
TYPE = (
    ("CUSTOMER", "CUSTOMER"),
    ("RIDER", "RIDER"),
    ("ADMIN", "ADMIN"),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    type = models.CharField(max_length=50, choices=TYPE)