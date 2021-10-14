# Generated by Django 3.1.13 on 2021-10-14 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
import jobposts.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='slug')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='slug')),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField()),
                ('company_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('lindkedin_url', models.URLField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('how_to_apply', models.TextField()),
                ('application_url', models.URLField(blank=True, null=True)),
                ('application_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[(jobposts.models.StatusChoice['NEW'], 'new'), (jobposts.models.StatusChoice['APPROVED'], 'approved'), (jobposts.models.StatusChoice['DELETED'], 'deleted'), (jobposts.models.StatusChoice['EXPIRED'], 'expired')], default=jobposts.models.StatusChoice['NEW'], max_length=20)),
                ('job_type', models.CharField(choices=[(jobposts.models.JobTypeChoice['PART_TIME'], 'Part Time'), (jobposts.models.JobTypeChoice['FULL_TIME'], 'Full Time'), (jobposts.models.JobTypeChoice['CONTRACT'], 'Contract'), (jobposts.models.JobTypeChoice['INTERNSHIP'], 'Internship')], max_length=20)),
                ('currency', models.CharField(choices=[(jobposts.models.CurrencyChoice['PESOS'], 'DOP'), (jobposts.models.CurrencyChoice['DOLLARS'], 'USD'), (jobposts.models.CurrencyChoice['EUROS'], 'EUR')], max_length=20)),
                ('salary_range_start_at', models.IntegerField(blank=True, null=True)),
                ('salary_range_end_at', models.IntegerField(blank=True, null=True)),
                ('sponsor_relocation', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobposts.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobposts.company')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
