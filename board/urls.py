from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("", views.kanban_board, name="kanban"),
    path("documents/", views.document_catalog, name="documents"),
    path("documents/add/", views.add_document, name="add_document"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/<int:task_id>/edit/", views.update_task, name="update_task"),
    path("tasks/<int:task_id>/status/", views.update_task_status, name="update_task_status"),
    path("tasks/<int:task_id>/subtasks/add/", views.add_subtask, name="add_subtask"),
    path("subtasks/<int:subtask_id>/toggle/", views.toggle_subtask, name="toggle_subtask"),
]
