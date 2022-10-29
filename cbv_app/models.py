from django.db import models
from django.urls import reverse
# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=19)
    emp_salary=models.IntegerField()
    emp_email=models.EmailField()
    emp_designation=models.CharField(max_length=29)

    def __str__(self):
        return self.emp_name

    def get_absolute_url(self):

        return reverse('list')
