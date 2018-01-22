from django.contrib import admin

# Register your models here.

from .models import *
from django.forms import TextInput, Textarea
from django.db import models
from tinymce.widgets import TinyMCE

class ReportModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        #models.TextField: {'widget':TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
admin.site.register(Report, ReportModelAdmin)

admin.site.register(ReportStatus)
admin.site.register(ReportType)
admin.site.register(ReportRenderingStrategy)
admin.site.register(ReportRelationshipType)
admin.site.register(Company)

admin.site.register(ReportCompany)
admin.site.register(ReportReport)
