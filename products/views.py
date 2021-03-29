from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.template import loader
from products.models import Product



class ProductView(View):
    def get(self,request, *args, **kwargs):
        products = Product.objects.values('category').distinct()
        context = {
            "product_list": products
        }
        return render(request, "products/index.html", context)

class ProductCategoryView(View):
    def get(self,request, category, *args, **kwargs):
        if request.is_ajax():
            products = Product.objects.filter(category=category)
            context = {
                "product_image_list": products
            }
            template = loader.get_template("products/category.html")
            return HttpResponse(template.render(context, self.request))
        return HttpResponse("Wrong request")
