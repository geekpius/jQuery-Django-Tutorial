from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views import View
from comments.forms import CommentForm
from comments.models import Comment

class CommentView(View):
    form_class = CommentForm
    def get(self, request, *args, **kwargs):
        return render(request, "comments/index.html", {})

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'success'})
            return JsonResponse({'message': 'Field couldn\'t validate'}) 
        return JsonResponse({'message': 'Wrong request'})

class CommentDataView(View):
    def get(self, request, *args, **kwargs):
        template = loader.get_template("comments/view.html")
        comments = Comment.objects.all()
        context = {
            "comment_list": comments
        }
        return HttpResponse(template.render(context, self.request))

