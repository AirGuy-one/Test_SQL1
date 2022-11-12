from django.contrib import admin
from .models import TestData, Categories, TestDataRelation, Like

admin.site.register(TestData)
admin.site.register(Categories)
admin.site.register(TestDataRelation)
admin.site.register(Like)


