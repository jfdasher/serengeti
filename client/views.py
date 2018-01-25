from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Report
from django.views.static import serve
from django.conf import settings
def index(request):
    current_reports_list = Report.objects.order_by('-release_date')[:5]
    context = {
        'current_reports_list': current_reports_list,
    }
    return render(request, 'reports/index.html', context)

def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    context = {
        'report': report,
    }
    if report.rendering_strategy.name == 'HTML_NOTE':
        return render(request, 'reports/note_detail.html', context)
    return serve(request, report.primary_file.url, '');
