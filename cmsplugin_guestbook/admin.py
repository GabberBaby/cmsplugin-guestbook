from django.contrib import admin
from . import models

def publish(modeladmin, request, queryset):
    for object in queryset:
        object.publish()
publish.short_description = 'Publish'

def unpublish(modeladmin, request, queryset):
    for object in queryset:
        object.unpublish()
unpublish.short_description = 'Unpublish'

class GuestbookAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_public']
    list_filter = ['is_public']
    actions = [publish, unpublish]

admin.site.register(models.Guestbook, GuestbookAdmin)
