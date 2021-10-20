from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class State(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class covidvacc(models.Model):
    name = models.CharField(max_length=100)
    Age = models.DateField(null=True, blank=True)
    District = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    State = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name