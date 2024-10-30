from django.contrib import admin

# Register your models here.
from .models import AnnouncedPuResults
from .models import PollingUnit


admin.site.register(AnnouncedPuResults)
admin.site.register(PollingUnit)
