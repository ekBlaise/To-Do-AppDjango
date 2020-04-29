from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views import generic
def index(request):
    tasks = Task.objects.order_by('-id').all()
    page = request.GET.get('page', 1)

    # Call the form that was created here
    form = TaskForm()

    # Check the form that is posted
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    # Testing pagination
    paginator = Paginator(tasks, 3)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    # Create a dictionary to hold all values
    context = {'tasks': tasks, 'form':form}
    return render(request, 'tasks/index.html', context)
# class IndexView(generic.ListView):
#     model = Task
#     template_name = 'tasks/index.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'tasks'  # Default: object_list
#     paginate_by = 4
#     queryset = Task.objects.all()

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    # Create an instance of the task
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)