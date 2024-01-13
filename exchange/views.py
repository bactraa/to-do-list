from django.shortcuts import render, get_object_or_404
from .models import ToDo
from forms import ToDoForm


def index(request):
    todos = ToDo.objects.all()
    context = {'todos':todos}
    return render(request, 'index.html', context)



def detail(request, pk):
    todo = get_object_or_404(ToDo, id = pk)
    context = {'func': todo}
    return render(request, 'detail.html', context)


def add(request):
    form = ToDoForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}