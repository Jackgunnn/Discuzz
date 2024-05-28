from django.contrib import admin

from questions.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
# class QuestionAdmin(admin.ModelAdmin):
#     readonly_fields = ['asked_at']
#
# admin.site.register(Question, QuestionAdmin)