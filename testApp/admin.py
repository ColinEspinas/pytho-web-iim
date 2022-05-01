from dataclasses import fields
from django.contrib import admin

from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
  fields=['text']

admin.site.register(Question)