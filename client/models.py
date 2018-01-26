from django.db import models
from tinymce import models as tinymce_models
import datetime

class ReportStatus(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "Report Statuses"

    def __str__(self):
        return self.name

class ReportType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class FlashRating(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class ProductLine(models.Model):
    DEFAULT_PK=1
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class ReportRenderingStrategy(models.Model):
    DEFAULT_PK=1
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Report Rendering Strategies"

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
        return self.name +  " : " + self.ticker

class Tag(models.Model):
    name = models.CharField(max_length=12)

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)

    text = models.TextField(null=True, blank=True)
    headline = models.TextField(null=True, blank=True)
    story = models.TextField(null=True, blank=True)

    sub_heading = models.TextField(null=True, blank=True)
    sources = models.CharField(null=True, blank=True, max_length=2000)

    release_date = models.DateField('date published', default=datetime.date.today)
    status = models.ForeignKey(ReportStatus, on_delete=models.PROTECT)
    product_line = models.ForeignKey(ProductLine, on_delete=models.PROTECT, default=2)
    rendering_strategy = models.ForeignKey(ReportRenderingStrategy, on_delete=models.PROTECT, default=2)
    tickers = models.ManyToManyField(
        Company,
        through='ReportCompany'
    )
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    flash_parent = models.ForeignKey("self", related_name="flash_children", null=True, blank=True, on_delete=models.PROTECT)
    flash_rating = models.ForeignKey(FlashRating, null=True, blank=True, on_delete=models.PROTECT)
    source_parent = models.ForeignKey("self", related_name="source_children", null=True, blank=True, on_delete=models.PROTECT)
    previous_report = models.ForeignKey("self", related_name="later_reports", null=True, blank=True, on_delete=models.PROTECT)
    primary_file = models.FileField(null=True, blank=True)
    source_file = models.FileField(null=True, blank=True)
    def __str__(self):
        return "%s : %s" % (self.title,  str(self.release_date))
    def primary_tickers(self):
        return Company.objects.filter(report_mention__primary=True, report_mention__report=self).all()
    def secondary_tickers(self):
        return Company.objects.filter(report_mention__primary=False, report_mention__report=self).all()


class ReportCompany(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='report_mention')
    primary = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Report Companies"

#class ReportReport(models.Model):
#    parent = models.ForeignKey(Report, related_name="children",  on_delete=models.CASCADE)
#    child = models.ForeignKey(Report, related_name="parents",  on_delete=models.CASCADE)
#    relationship = models.ForeignKey(ReportRelationshipType, on_delete=models.PROTECT)

#class ReportFileType(models.Model):
#    DEFAULT_PK=1
#    name = models.CharField(max_length=32)
#    def __str__(self):
#        return self.name

#class ReportFile(models.Model):
#    report = models.ForeignKey(Report, on_delete=models.CASCADE)
#    type = models.ForeignKey(ReportFileType, on_delete=models.PROTECT)
#    file = models.FileField()



"""

"""

# Create your models here.

"""
class ReportRelationship(models.Model):
    parent = models.ForeignKey(Report, related_name="parent", on_delete=models.CASCADE)
    child = models.ForeignKey(Report, related_name="child",  on_delete=models.CASCADE)
    type = models.ForeignKey(ReportRelationshipType, on_delete=models.PROTECT)
"""
