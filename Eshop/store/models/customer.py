from django.db import models



class Customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.BigIntegerField()
    password = models.CharField(max_length=20)

    def ifExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False