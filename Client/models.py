from django.db import models
from user.models import user
# Create your models here.
class client(models.Model):
    client_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(user,on_delete=models.CASCADE)


    def __str__(self):
        return self.client_name

    