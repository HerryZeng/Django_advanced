from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, View

from .models import Task,Poem


# Create your views here.

def home(request):
    user_list = User.objects.all()
    tasklist='/tasklist/'
    poemlist='/poemlist/'
    add_task = '/add_task/'
    add_poem = '/add_poem/'
    return render(request, 'firstapp/table.html', locals())


def index(request):
    return render(request, 'firstapp/index.html')


class IndexView(TemplateView):
    template_name = 'firstapp/index.html'


class ShowTasksView(ListView):
    template_name = 'firstapp/tasks.html'
    model = Task

class ShowPoemView(ListView):
    template_name = 'firstapp/poems.html'
    model = Poem

class DisplaySingleView(TemplateView):
    template_name = 'firstapp/single_task.html'

    def get_context_data(self, **kwargs):
        context = super(DisplaySingleView, self).get_context_data(**kwargs)
        task_id = self.kwargs.get('task_id', 0)
        context['task'] = Task.objects.get(task_id=task_id)
        return context


class AddModelView(View):
    # def __init__(self,form_class, template_name):
    form_class = ""
    template_name = ""
    return_url = " "

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        # global return_url
        if form.is_valid():
            form.save()
        # return HttpResponse("添加成功")
        return HttpResponseRedirect(self.return_url)
