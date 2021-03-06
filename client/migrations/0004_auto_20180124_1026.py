# Generated by Django 2.0.1 on 2018-01-24 15:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20180122_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='type',
        ),
        migrations.AlterField(
            model_name='report',
            name='previousReport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='later_reports', to='client.Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='release_date',
            field=models.DateField(default=datetime.date.today, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='report',
            name='sourceParent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='source_children', to='client.Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='report',
            name='product_line',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='client.ProductLine'),
        ),
    ]
