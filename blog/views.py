from django.shortcuts import render, redirect
import re
from django.utils.timezone import datetime
from django.views.generic import ListView
from blog.forms import LogMessageForm
from blog.models import LogMessage

# Create your views here.
class HomeListView(ListView):
    """Renders the home page with a list of log messages"""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(request, 'blog/hello_there.html',{
        'name': name,
        'date':datetime.now()
    })

def software(request):
    return render(request, 'blog/software.html')

def cloud(request):
    return render(request, 'blog/cloud.html')

def data(request):
    return render(request, 'blog/data.html')

def it_ops(request):
    return render(request, 'blog/it_ops.html')

def leadership(request):
    return render(request, 'blog/leadership.html')

def security(request):
    return render(request, 'blog/security.html')





def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "blog/log_message.html", {'form': form})