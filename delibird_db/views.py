from django.shortcuts import render
from delibird_db.models import Table
from delibird_db.serializers import TableSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def table_manager(request):

    if request.method == 'GET':
        tables = Table.objects.all()
        table_id = request.query_params.get('table_id', None)
        if table_id is not None:
            tables = tables.filter(id=table_id)
        tables_serializer = TableSerializer(tables, many=True)
        return JsonResponse(tables_serializer.data, safe=False)

    if request.method == 'POST':
        pos_x_data = request.GET['pos_x']
        pos_y_data = request.GET['pos_y']
        angle_z_data = request.GET['angle_z']
        angle_w_data = request.GET['angle_w']
        table_obj = Table(pos_x=pos_x_data, pos_y=pos_y_data, angle_z=angle_z_data, angle_w=angle_w_data)
        table_obj.save()
        tables = Table.objects.all()
        tables_serializer = TableSerializer(tables, many=True)
        return JsonResponse(tables_serializer.data, safe=False)



 

    
