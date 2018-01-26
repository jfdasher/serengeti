from ajax_select import register, LookupChannel
from .models import Report

@register('reports')
class ReportLookup(LookupChannel):

    model = Report

    def get_query(self, q, request):
        return self.model.objects.filter(title__icontains=q).order_by('title')[:50]
