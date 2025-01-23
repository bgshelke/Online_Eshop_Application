from django.db import models

class Catagory(models.Model):
    objects = None
    name=models.CharField(max_length=50)


    def __str__(self) -> str:
        return f'{self.name}'