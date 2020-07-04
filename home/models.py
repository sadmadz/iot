from django.db import models


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=60)
    name = models.CharField(max_length=60)


class Thing(models.Model):
    id = models.AutoField(primary_key=True)
    home = models.ForeignKey(Home, related_name='things', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=1)
    description = models.CharField(null=True, blank=True, max_length=1000)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    thing_row = models.DecimalField(max_digits=3, decimal_places=0)
    thing_column = models.DecimalField(max_digits=3, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)
