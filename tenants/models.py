from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
#from managers.models import Manager, Property


class Tenant(models.Model):
    pass


class TenantReview(models.Model):
    manager = models.ForeignKey(
        Tenant, on_delete=models.CASCADE, null=True, blank=True)
    author_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250)
    phone = ""
    review_text = models.TextField(max_length=500)
    rating = ""
