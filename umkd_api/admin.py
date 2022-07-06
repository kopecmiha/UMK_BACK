from django.contrib import admin

from umkd_api.models import Competence, Indicator


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    """
    Competence
    """

    list_display = "code", "description"
    list_display_links = "code", "description"
    search_fields = "code", "description"


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    """
    Indicator
    """

    list_display = "code", "description", "type"
    list_display_links = "code", "description", "type"
    search_fields = "code", "description", "type"
