from django.contrib import admin

# Register your models here.
from .models import Image
from .models import Comment

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['text']

    