from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
# from django.shortcuts import render, redirect
# from django.template import loader


class TaskView(View):
    form_class = TaskForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "success"})
            return JsonResponse({"message": "Validation failed"})
        return JsonResponse({"message": "Wrong request"})

    def get(self,request, *args, **kwargs):
        return render(request, "index.html", {})

class ViewTaskView(View):

    def get(self,request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, "view.html", {"tasks":tasks})

class TaskDeleteView(View):
    
    def get(self,request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong request"})
