from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
from django.core import serializers


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

class TaskUpdateDeleteView(View):
    form_class = TaskForm

    def get(self, request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong route"})

    def post(self, request, pk, *args, **kwargs):
        if request.is_ajax():
            task = Task.objects.get(pk=pk)
            data = {
                "owner":task.owner, 
                "name":task.name, 
                "task_date":task.task_date, 
                "start_time": task.start_time,
                "end_time": task.end_time
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                owner = form.cleaned_data['owner']
                name = form.cleaned_data['name']
                task_date = form.cleaned_data['task_date']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']

                if form.has_changed():
                    task.owner = owner
                    task.name = name
                    task.task_date = task_date
                    task.start_time = start_time
                    task.end_time = end_time
                    task.save()
                    return JsonResponse({'message':'success'})
                    
                return JsonResponse({'message': 'Data is not editted'})

            return JsonResponse({'message': 'Validation failed'})

        return JsonResponse({'message': 'Wrong request'})


class TutorialView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "tutorial.html", {})

class TutorialDataView(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            tasks = Task.objects.all()
            task_serializers = serializers.serialize('json', tasks)
            return JsonResponse(task_serializers, safe=False)
        return JsonResponse({'message':'Wrong request'})


    