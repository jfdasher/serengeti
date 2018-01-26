from django.contrib import admin

# Register your models here.

from .models import *
from django.forms import TextInput, Textarea
from django.db import models
#from tinymce.widgets import TinyMCE

class ReportCompanyInline(admin.TabularInline):
    model = ReportCompany
    extra = 1

class ReportFlashInline(admin.TabularInline):
     model=Report
     fk_name='flash_parent'
     extra = 0
#    model = ReportReport
#    fk_name = 'parent'
#    extra = 1


#class ReportReportInline(admin.TabularInline):
#    model = ReportReport
#    fk_name = 'parent'
#    extra = 1

#class ReportFileInline(admin.TabularInline):
#    model = ReportFile
#    extra = 1

from tinymce.widgets import TinyMCE
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

@admin.register(Report)
class ReportModelAdmin(AjaxSelectAdmin):
    inlines = (ReportCompanyInline,
               ReportFlashInline,
    )
    list_display = ('title', 'release_date', 'status', 'product_line', 'rendering_strategy')

    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()},
    }
    form = make_ajax_form(Report, {
        'flash_parent': 'reports',  # ManyToManyField
    })



#admin.site.register(Report)

admin.site.register(ReportStatus)
admin.site.register(ReportType)
admin.site.register(ReportRenderingStrategy)
#admin.site.register(ReportRelationshipType)
admin.site.register(Company)
admin.site.register(ProductLine)

#admin.site.register(ReportFileType)
