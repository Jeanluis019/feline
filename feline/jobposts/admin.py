from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from .models import Category, Company, JobPost

admin.site.register(Category, SimpleHistoryAdmin)
admin.site.register(Company, SimpleHistoryAdmin)
admin.site.register(JobPost, SimpleHistoryAdmin)
