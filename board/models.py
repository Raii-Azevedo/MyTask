from django.db import models


class Task(models.Model):
	STATUS_TODO = "todo"
	STATUS_DOING = "doing"
	STATUS_DONE = "done"
	PRIORITY_HIGH = "alta"
	PRIORITY_MEDIUM = "media"
	PRIORITY_LOW = "baixa"

	STATUS_CHOICES = (
		(STATUS_TODO, "To Do"),
		(STATUS_DOING, "Doing"),
		(STATUS_DONE, "Done"),
	)

	PRIORITY_CHOICES = (
		(PRIORITY_HIGH, "Alta"),
		(PRIORITY_MEDIUM, "Media"),
		(PRIORITY_LOW, "Baixa"),
	)

	title = models.CharField(max_length=180)
	description = models.TextField(blank=True)
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
	deadline = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_TODO)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self):
		return self.title


class SubTask(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
	title = models.CharField(max_length=180)
	is_done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["created_at"]

	def __str__(self):
		return self.title


class DocumentLink(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=500)
	client = models.CharField(max_length=160)
	reference_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-reference_date", "-created_at"]

	def __str__(self):
		return f"{self.title} - {self.client}"
