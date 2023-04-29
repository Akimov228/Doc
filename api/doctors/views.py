from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from .models import Doctor, Specialty
from .serializers import DoctorSerializer, DoctorValidateSerializer, SpecialtySerializer, SpecialtyValidateSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404


class DoctorListCreateAPIView(ListCreateAPIView):
    """List of objects"""
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'pk'
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['full_name', 'specialties__name', 'clinic__name', 'category_services__name']

    """Creation of objects"""
    def post(self, request, *args, **kwargs):
        serializer = DoctorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        photo = request.data.get('photo')
        fullname = request.data.get('full_name')
        specialties = request.data.get('specialties')
        experience = request.data.get('experience')
        clinic = request.data.get('clinic')
        clinic_id = request.data.get('clinic_id')
        price = request.data.get('price')
        summary = request.data.get('summary')
        # category_services = request.data.get('category_services')

        doctor = Doctor.objects.create(photo=photo, full_name=fullname,specialties=specialties, experience=experience,clinic_id=clinic_id, clinic=clinic, price=price, summary=summary)

        return Response(data={'message': 'Data received',
                              'doctor': DoctorSerializer(doctor).data},
                        status=status.HTTP_201_CREATED)

class DoctorDetailAPIView(APIView):
    def get(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(data=serializer.data)

    def delete(self, request, id):
        doctor = self.get_object(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if any fields were provided in the request data
        if not any(request.data.values()):
            return Response(data={'detail': 'At least one field is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Update the doctor object with the provided data
        if request.data.get('photo'):
            doctor.photo = request.data['photo']
        if request.data.get('fullname'):
            doctor.full_name = request.data['fullname']
        if request.data.get('experience'):
            doctor.experience = request.data['experience']
        if request.data.get('price'):
            doctor.price = request.data['price']
        if request.data.get('summary'):
            doctor.summary = request.data['summary']
            doctor.save()

        serializer = DoctorSerializer(doctor)
        return Response(data={'message': 'Data received',
                              'doctor': serializer.data},
                        status=status.HTTP_200_OK)

    def get_object(self, id):
        doctor = get_object_or_404(Doctor, id=id)
        return doctor


class SpecialtiesListCreateAPIView(ListCreateAPIView):
    '''list of objects'''
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

    '''creation of objects'''
    def post(self, request, *args, **kwargs):
        serializer = SpecialtyValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        specialty = Specialty.objects.create(name=name)
        return Response(data={'message': 'Data received',
                              'specialty': SpecialtySerializer(specialty).data},
                        status=status.HTTP_201_CREATED)


class DetailAPIView(APIView):
    def get(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(data=serializer.data)

    def delete(self, request, id):
        doctor = self.get_object(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        doctor = self.get_object(id)
        serializer = DoctorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if any fields were provided in the request data
        if not any(request.data.values()):
            return Response(data={'detail': 'At least one field is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Update the doctor object with the provided data
        if request.data.get('photo'):
            doctor.photo = request.data['photo']
        if request.data.get('fullname'):
            doctor.full_name = request.data['fullname']
        if request.data.get('experience'):
            doctor.experience = request.data['experience']
        if request.data.get('price'):
            doctor.price = request.data['price']
        if request.data.get('summary'):
            doctor.summary = request.data['summary']
            doctor.save()

        serializer = DoctorSerializer(doctor)
        return Response(data={'message': 'Data received',
                              'doctor': serializer.data},
                        status=status.HTTP_200_OK)

    def get_object(self, id):
        doctor = get_object_or_404(Doctor, id=id)
        return doctor

