from django.db import models
from tinymce import models as tinymce_models
import datetime

class ReportStatus(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class ReportType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class ReportRenderingStrategy(models.Model):
    DEFAULT_PK=1
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class ReportRelationshipType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=32)
    private = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Companies"
    def __str__(self):
        return self.name +  " " + self.ticker



# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    release_date = models.DateField('date published', default=datetime.date.today)
    status = models.ForeignKey(ReportStatus, on_delete=models.PROTECT)
    type = models.ForeignKey(ReportType, on_delete=models.PROTECT)
    rendering_strategy = models.ForeignKey(ReportRenderingStrategy, on_delete=models.PROTECT, null=True)
    private = models.BooleanField(default=False)
    tickers = models.ManyToManyField(
        Company,
        through='ReportCompany'
    )
    sourceParent = models.ForeignKey("self", related_name="source_children", null=True, on_delete=models.PROTECT)
    previousReport = models.ForeignKey("self", related_name="later_reports", null=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.title + ": " + self.release_date


class ReportCompany(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    primary = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Report Companies"

class ReportReport(models.Model):
    parent = models.ForeignKey(Report, related_name="children",  on_delete=models.CASCADE)
    child = models.ForeignKey(Report, related_name="parents",  on_delete=models.CASCADE)
    relationship = models.ForeignKey(ReportRelationshipType, on_delete=models.PROTECT)

"""

"""

# Create your models here.

"""
class ReportRelationship(models.Model):
    parent = models.ForeignKey(Report, related_name="parent", on_delete=models.CASCADE)
    child = models.ForeignKey(Report, related_name="child",  on_delete=models.CASCADE)
    type = models.ForeignKey(ReportRelationshipType, on_delete=models.PROTECT)
"""
