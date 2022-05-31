from multiprocessing import context
from sqlite3 import Time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import ToDoItem
from datetime import datetime
# Create your views here.
def index(request):
   #Home Page
   done_item = ToDoItem.objects.filter(todo_status="Done")
   not_done_item = ToDoItem.objects.filter(todo_status="Not Done")
   context = {
     "done_item" : done_item,
     "not_done_item" : not_done_item,
     "count" : not_done_item.count()      #Time feature
   }

   return render(request,'todo_app/index.html',context)

def mark_all_complete(request):
     ToDoItem.objects.filter(todo_status="Not Done").update(todo_status="Done")
     return HttpResponseRedirect(reverse("todo_app:index"))

def insert_todo(request):
    #Insert Todo
    todo_text=request.POST["todo_text"]
    obj = ToDoItem(todo_text=todo_text)
    obj.save()
    return HttpResponseRedirect(reverse("todo_app:index"))

def mark_done(request,id):
    #Mark Done
    obj = ToDoItem.objects.get(id=id)
    obj.todo_status = "Done"
    obj.save()
    return HttpResponseRedirect(reverse("todo_app:index"))



def delete_todo(request,id):
   #Delete Todo
   obj = ToDoItem.objects.get(id=id)
   obj.delete() 
   return HttpResponseRedirect(reverse("todo_app:index"))

