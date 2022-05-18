import json
from django.http import HttpRequest, JsonResponse
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    '''DRF API VIEW'''
    data = {}
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        # print(serializer.data)
        data = serializer.data
        return Response(data)
    # return Response({"message":"Invalid data"},status=400)

@api_view(["GET"])
def api_home_get(request: HttpRequest, *args, **kwargs):
    '''DRF API VIEW'''
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # The above assigning makes the serialization
        # model instance -> dict -> return json to client
        # data = model_to_dict(instance,fields=["title","content","price","sale_price"])

    if instance:
        data = ProductSerializer(instance).data
    
    return Response(data)

def api_home_django(request: HttpRequest, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # The above assigning makes the serialization
        # model instance -> dict -> return json to client
        data = model_to_dict(model_data,fields=["title","content","price"])
    return JsonResponse(data)
