# Generated by Django 2.2.4 on 2019-09-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsite', '0003_auto_20190902_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='cover_letter_attachment',
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='JobSite!', max_length=50),
        ),
    ]