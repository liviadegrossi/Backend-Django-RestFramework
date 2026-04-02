from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60, blank=False)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    code = models.CharField(max_length=10)
    description = models.TextField(blank=False)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.code
