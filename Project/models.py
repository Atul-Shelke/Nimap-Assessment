from django.db import models
from Client.models import client
from user.models import user
# Create your models here.
class project(models.Model):
    project_name=models.CharField(max_length=100)
    client=models.ForeignKey(client,on_delete=models.CASCADE,related_name='projects')
    users=models.ManyToManyField(user,related_name='projects')
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(user,on_delete=models.CASCADE)

    class Meta:
        db_table='project'