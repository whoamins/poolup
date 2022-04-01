from django.contrib import admin

from .models import Question, Choice


class _ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    fields = ['choice_text']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [_ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
