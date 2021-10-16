# Generated by Django 3.1.13 on 2021-10-16 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobposts', '0002_insert_category_default_values'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalJobPost',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('how_to_apply', models.TextField()),
                ('application_url', models.URLField(blank=True, null=True)),
                ('application_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('approved', 'Approved'), ('deleted', 'Deleted'), ('expired', 'Expired')], default='new', max_length=20)),
                ('job_type', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Contract', 'Contract'), ('Internship', 'Internship')], max_length=20)),
                ('currency', models.CharField(choices=[('DOP', 'Pesos'), ('USD', 'Dollars'), ('EUR', 'Euros')], max_length=20)),
                ('salary_range_start_at', models.IntegerField(blank=True, null=True)),
                ('salary_range_end_at', models.IntegerField(blank=True, null=True)),
                ('sponsor_relocation', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='jobposts.category')),
                ('company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='jobposts.company')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical job post',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('logo', models.TextField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='slug')),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField()),
                ('company_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('lindkedin_url', models.URLField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical company',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', verbose_name='slug')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical category',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]