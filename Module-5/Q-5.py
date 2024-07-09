#Q-5. What is a QuerySet?Write program to create a new Post object in
#     database:

'''
A QuerySet represents a collection of objects from your database.
It can have zero, one or many filters. Filters narrow down the query 
results based on the given parameters. In SQL terms, a QuerySet equates 
to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT.

from django.db import models

# Create your models here.
class manpower(models.Model):
    uname = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=20)
    age = models.CharField(max_length=10)


'''


