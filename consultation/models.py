from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Account

class Consult(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    name_of_consult = models.CharField(max_length=200)
    prescription = models.CharField(max_length=200)
    date_of_consult = models.DateTimeField(auto_now_add=True)