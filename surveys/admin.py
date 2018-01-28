from django.contrib import admin
from surveys.models import SurveyType, Survey


class SurveyTypeAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'title', 'fields')
    readonly_fields = ('slug',)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'completed_at', 'completed', 'survey_type', 'rcpt', 'external_url')
    readonly_fields = ('external_url', )
    list_filter = ('completed', )


admin.site.register(SurveyType, SurveyTypeAdmin)
admin.site.register(Survey, SurveyAdmin)

