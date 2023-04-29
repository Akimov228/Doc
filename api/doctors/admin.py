# global imports
from django.contrib import admin

# local imports
from .models import *


admin.site.register(Doctor)
admin.site.register(Specialty)
admin.site.register(Category)
admin.site.register(Clinic)
