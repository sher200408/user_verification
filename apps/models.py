from django.db import models
# ORM - Object Relational Mapper
# Create your models here.

#
# class UserLogin(models.Model):
#     last_name = models.CharField(max_length=150)
#     first_name = models.CharField(max_length=150)
#     middle_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=120)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#            return self.last_name
