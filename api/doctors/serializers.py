from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Specialty, Doctor, Clinic, Category


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id', 'name']

class SpecialtyValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=40, min_length=1)

    def validate_specialties_id(self, id):
        try:
            Specialty.objects.filter(id=id)
        except Specialty.DoesNotExist:
            raise ValidationError('This specialty does not exist!')


class DoctorSerializer(serializers.ModelSerializer):
    specialties = SpecialtySerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'photo', 'full_name', 'specialties',
                  'experience', 'clinic', 'price', 'summary', 'category_services']


class DoctorValidateSerializer(serializers.Serializer):
    photo = serializers.ImageField(required=False)
    full_name = serializers.CharField(required=True, max_length=100)
    specialties = serializers.CharField(required=False, max_length=40, min_length=1)
    experience = serializers.IntegerField(required=True, max_value=50.0, min_value=0.0)
    # clinic = serializers.CharField(max_length=40, min_length=1)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    summary = serializers.CharField(max_length=1000, min_length=0)
    # category_services = serializers.CharField(max_length=50)


    def validate_doctor_id(self, doctor_id):
        try:
            Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            raise ValidationError('This doctor does not exist!')


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['name', 'address']


class ClinicValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=40, min_length=1)
    address = serializers.CharField(required=True, max_length=40, min_length=1)


class CategoryServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CategoryServiceValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=50)