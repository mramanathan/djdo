# -*- coding: utf-8 -*-

from django import forms

class TodoForm(forms.Form):
	name = forms.CharField(max_length=255, min_length=5,  required=True)
	is_completed = forms.BooleanField(required=False)
	notes = forms.CharField(widget=forms.Textarea, required=False)
	due_date = forms.DateTimeField(required=True)

class TodoDeleteForm(forms.Form):
	pass
