from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.template import loader
from products.models import Product



class TutorialView(View):
    def get(self,request, *args, **kwargs):
        products = Product.objects.values('category').distinct()
        context = {
            "product_list": products
        }
        return render(request, "tutorial/index.html", context)

class GetProductView(View):
    def get(self,request, category, *args, **kwargs):
        if request.is_ajax():
            products = Product.objects.filter(category=category).values('id', 'name')
            return JsonResponse({'data': list(products)})
        return HttpResponse('Wrong request')