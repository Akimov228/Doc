from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Clinic(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True)
    specialties = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='doctors_specialties')
    experience = models.PositiveSmallIntegerField()
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctor_clinics')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    summary = models.CharField(max_length=1000, null=True)
    category_services = models.ManyToManyField(Category, related_name='doctor_services')

    def __str__(self):
        return self.full_name

