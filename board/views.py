from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import DocumentLinkForm, SubTaskForm, TaskForm, TaskStatusForm, TaskUpdateForm
from .models import DocumentLink, SubTask, Task


def kanban_board(request):
	tasks = Task.objects.prefetch_related("subtasks")
	grouped = {status: [] for status, _ in Task.STATUS_CHOICES}

	for task in tasks:
		grouped[task.status].append(task)

	columns = [
		{
			"key": status,
			"label": label,
			"tasks": grouped[status],
		}
		for status, label in Task.STATUS_CHOICES
	]

	context = {
		"columns": columns,
		"task_form": TaskForm(),
		"subtask_form": SubTaskForm(),
		"status_choices": Task.STATUS_CHOICES,
		"today": timezone.localdate(),
	}
	return render(request, "board/kanban.html", context)


@require_POST
def add_task(request):
	form = TaskForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect("board:kanban")


@require_POST
def update_task_status(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	form = TaskStatusForm(request.POST, instance=task)
	if form.is_valid():
		form.save()
	return redirect("board:kanban")


@require_POST
def update_task(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	form = TaskUpdateForm(request.POST, instance=task)
	if form.is_valid():
		form.save()
	return redirect("board:kanban")


@require_POST
def add_subtask(request, task_id):
	task = get_object_or_404(Task, id=task_id)
	form = SubTaskForm(request.POST)
	if form.is_valid():
		subtask = form.save(commit=False)
		subtask.task = task
		subtask.save()
	return redirect("board:kanban")


@require_POST
def toggle_subtask(request, subtask_id):
	subtask = get_object_or_404(SubTask, id=subtask_id)
	subtask.is_done = not subtask.is_done
	subtask.save(update_fields=["is_done"])
	return redirect("board:kanban")


def document_catalog(request):
	query = request.GET.get("q", "").strip()
	documents = DocumentLink.objects.all()

	if query:
		documents = documents.filter(
			Q(title__icontains=query)
			| Q(client__icontains=query)
			| Q(url__icontains=query)
		)

	context = {
		"document_form": DocumentLinkForm(),
		"documents": documents,
		"query": query,
	}
	return render(request, "board/documents.html", context)


@require_POST
def add_document(request):
	form = DocumentLinkForm(request.POST)
	if form.is_valid():
		form.save()
	return redirect("board:documents")
