from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .forms import TodoListForm
from .models import tododata
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Todoapp(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data['item'])
            username_v = request.user.username
            item_v = form.cleaned_data['item']
            data = tododata(username=username_v,item=item_v)
            data.save()
            all_items = tododata.objects.all().filter(username=username_v)
            messages.success(request,('Item has been added to list'))
            return render(request,'home.html',{'all_items':all_items,'form':form})
    else:
        username_v = request.user.username
        all_items = tododata.objects.all().filter(username=username_v)
        form = TodoListForm()
        return render(request,'home.html',{'all_items':all_items,'form':form})


def deleteview(request,todo_id):
    item = tododata.objects.get(pk=todo_id)
    item.delete()
    messages.success(request,('item has been deleted'))
    return redirect('todoview')

def cross_off(request,todo_id):
    item = tododata.objects.get(pk = todo_id)
    item.completed = True
    item.save()
    return redirect('todoview')

def uncross(request,todo_id):
    item =tododata.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect('todoview')