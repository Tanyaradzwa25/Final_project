from django.db import models


GENDER_CHOICES = (
    ('Select', 'Select'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

ADMISSION_CHOICES =(
    ('Select' , 'Select'),
    ('Nil' , 'Nil'),
    ('Chris Hani Baragwanath Hospital (Johannesburg)' , 'Chris Hani Baragwanath Hospital (Johannesburg)'),
    ('Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)' , 'Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)'),
    ('Tygerberg Hospital (Cape Town)' , 'Tygerberg Hospital (Cape Town)'),
    ('Steve Biko Academic Hospital (Pretoria)' , 'Steve Biko Academic Hospital (Pretoria)'),
    ('Groote Schuur Hospital (Cape Town)' , 'Groote Schuur Hospital (Cape Town)'),
    ('Nelson Mandela Academic Hospital (Eastern Cape)' , 'Nelson Mandela Academic Hospital (Eastern Cape)'),
    ('Mamelodi Hospital (Gauteng)' , 'Mamelodi Hospital (Gauteng)'),
)
TRANSFER_CHOICES =(
    ('Select' ,'Select'),
    ('Nil' ,'Nil'),
    ('Chris Hani Baragwanath Hospital (Johannesburg)' ,'Chris Hani Baragwanath Hospital (Johannesburg)'),
    ('Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)' ,'Charlotte Maxeke Johannesburg Academic Hospital (Johannesburg)'),
    ('Tygerberg Hospital (Cape Town)' ,'Tygerberg Hospital (Cape Town)'),
    ('Steve Biko Academic Hospital (Pretoria)' ,'Steve Biko Academic Hospital (Pretoria)'),
    ('Groote Schuur Hospital (Cape Town)' ,'Groote Schuur Hospital (Cape Town)'),
    ('Nelson Mandela Academic Hospital (Eastern Cape)' ,'Nelson Mandela Academic Hospital (Eastern Cape)'),
    ('Mamelodi Hospital (Gauteng)' ,'Mamelodi Hospital (Gauteng)'),
)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Select')
    complain_details = models.TextField(null=True, blank=True)
    doctors_notes = models.TextField(null=True, blank=True)
    admission = models.CharField(max_length=200,choices=ADMISSION_CHOICES,default='Select')
    transfer = models.CharField(max_length=200,choices=TRANSFER_CHOICES,default='Select')

    def __str__(self):
        return self.name  
