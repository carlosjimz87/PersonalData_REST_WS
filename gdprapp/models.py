from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django_countries.fields import CountryField

GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


def validate_names(value):
    if value.isalpha() is False:
        raise ValidationError("Field is invalid!")
    # response = True;
    # for val in value.strip(" "):
    #     if val.isalpha() is False:
    #         response = False;
    #
    # if response is False:
    #     raise ValidationError('Field is invalid!')


def validate_birthdate(value):
    if int(datetime.date.today().year) - int(value.year) - 18 < 0:
        raise ValidationError("You must have a legal age!")


def validate_idcard(value):
    if value.isalnum() is False:
        raise ValidationError("Field is invalid!")


class GenderType(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Regex = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.Name


class IdType(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Regex = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.Name


class Subject(models.Model):
    ID = models.AutoField(primary_key=True)
    IdCard = models.CharField(max_length=10, blank=False, null=False, unique=True, validators=[validate_idcard])
    IdCardType = models.ForeignKey(IdType, on_delete=models.CASCADE, related_name='IdCardType', blank=False, null=False)
    Name = models.CharField(max_length=255, blank=False, null=False, validators=[validate_names])
    Surname = models.CharField(max_length=255, blank=False, null=False, validators=[validate_names])
    SecondSurname = models.CharField(max_length=255, blank=True, null=True, validators=[validate_names])
    Email = models.EmailField(max_length=255, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Country = CountryField(blank_label='(select country)')
    Gender = models.CharField(max_length=1, choices=GENDERS, default='F')
    BirthDate = models.DateField(validators=[validate_birthdate], null=False, blank=False)
    RegistrationDate = models.DateField(null=False, blank=False)
    ContactPermission = models.BooleanField(null=False)
    ConsentFilename = models.FileField(upload_to='consents', null=True, blank=True)

    def __str__(self):
        return '%s: (%s)' % (self.Name, self.IdCard)

