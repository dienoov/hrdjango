from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Division(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=64)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ("m", "Male"),
        ("f", "Female"),
    )
    STATUS_CHOICES = (
        ("permanent", "Permanent"),
        ("contract", "Contract"),
        ("internship", "Internship"),
    )
    name = models.CharField(max_length=64)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.name


class Role(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("employee", "Employee"),
    )
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)

    def __unicode__(self):
        return self.employee.name
