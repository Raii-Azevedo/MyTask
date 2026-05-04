from django.contrib import admin

from .models import DocumentLink, SubTask, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("title", "priority", "deadline", "status", "created_at")
	list_filter = ("priority", "status")
	search_fields = ("title", "description")


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
	list_display = ("title", "task", "is_done", "created_at")
	list_filter = ("is_done",)
	search_fields = ("title", "task__title")


@admin.register(DocumentLink)
class DocumentLinkAdmin(admin.ModelAdmin):
	list_display = ("title", "client", "reference_date", "updated_at")
	list_filter = ("client",)
	search_fields = ("title", "client", "url")
