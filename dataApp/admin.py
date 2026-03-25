from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author']
    ordering=['title']
    list_editable=['author']

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Comment)


