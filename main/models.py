import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=30, default='Uncategorized')