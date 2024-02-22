from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.


#Queryset
def aiquest_info(request):
    #complex data
    ai = Aiquest.objects.all()
    #python dict
    serializer = AiquestSerializer(ai, many=True)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')

#Model Instance
def aiquest_ins(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    #python dict
    serializer = AiquestSerializer(ai)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to steam python 
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #python to complex
        serializer = AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(res, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    

    if request.method == 'PUT':
        json_data = request.body
        #json to stream python 
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #python to complex
        serializer = AiquestSerializer(data=pythondata)
        id=pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully update data.'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(res, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')