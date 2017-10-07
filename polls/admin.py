# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 25
    date_hierarchy = 'pub_date'
    empty_value_display = '-empty-'


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('Choice', {'fields': ['choice_text']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
