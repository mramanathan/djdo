from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

# Create your views here.

from todo.models import Todo
from .forms import TodoForm, TodoDeleteForm

def index(request):
	return HttpResponse('hello world')

def todo_list(request):
	todos = Todo.objects.all()
	context = {'todos' : todos}
	return render(request, 'todo/todo_list.html',
		      context)

def todo_detail(request, pk):
	todo = get_object_or_404(Todo, pk=pk)
	context = {'todo' : todo}
	return render(request, 'todo/todo_detail.html',
		      context)

def todo_new(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			# todo = Todo.objects.create(form_data['name'])
			todo = Todo(name=form_data['name'],
				    is_completed =form_data['is_completed'],
				    notes=form_data['notes'],
				    due_date=form_data['due_date'])
			todo.save()
			return redirect('todo_detail', pk=todo.pk)
		context = {'todo' : form, 'url' : reverse('todo_new')}
		return render(request, 'todo/todo_new.html',
			      context)
	elif request.method == 'GET':
		form = TodoForm()
		context = {'form' : form, 'url' : reverse('todo_new')}
		return render(request, 'todo/todo_new.html',
			      context)


def todo_edit(request, pk):
	if request.method == 'GET':
		todo = get_object_or_404(Todo, pk=pk)
		data = {'name' : todo.name,
			'is_completed' : todo.is_completed,
			'notes' : todo.notes,
			'due_date' : todo.due_date}
		form = TodoForm(initial=data)
		context = {'form' : form, 'url' : reverse('todo_edit', args=(todo.id,))}
		return render(request, 'todo/todo_new.html',
			      context)
	elif request.method == 'POST':
		todo = get_object_or_404(Todo, pk=pk)
		form = TodoForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			todo.name = data['name']
			todo.is_completed = data['is_completed']
			todo.notes = data['notes']
			todo.due_date = data['due_date']
			todo.save()
			return redirect('todo_list')
		context = {'form' : form, 'url' : reverse('todo_edit', args=(todo.id,))}
		return render(request, 'todo/todo_new.html',
				      context)


def todo_delete(request, pk):
	if request.method == 'GET':
		todo = get_object_or_404(Todo, pk=pk)
		form = TodoDeleteForm()
		context = {'form' : form, 'url' : reverse('todo_delete', args=(todo.id,)), 'todo' : todo}
		return render(request, 'todo/todo_delete.html',
			      context)
	elif request.method == 'POST':
		form = TodoDeleteForm(request.POST)
		if form.is_valid():
			todo = get_object_or_404(Todo, pk=pk)
			todo.delete()
			return redirect('todo_list')
		context = {'form' : form, 'url' : reverse('todo_delete', args=(todo.id,))}
		return render(request, 'todo/todo_delete.html',
				      context)


