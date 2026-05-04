from django import forms

from .models import DocumentLink, SubTask, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "deadline", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Titulo da task"}),
            "description": forms.Textarea(attrs={"rows": 3, "placeholder": "Descricao (opcional)"}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "deadline"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Titulo"}),
            "description": forms.Textarea(attrs={"rows": 2, "placeholder": "Descricao"}),
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Nova subtarefa"}),
        }


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["status"]


class DocumentLinkForm(forms.ModelForm):
    class Meta:
        model = DocumentLink
        fields = ["title", "url", "client", "reference_date"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Titulo do documento"}),
            "url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "client": forms.TextInput(attrs={"placeholder": "Nome do cliente"}),
            "reference_date": forms.DateInput(attrs={"type": "date"}),
        }
