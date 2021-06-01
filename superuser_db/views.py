from django.shortcuts import render
from superuser_db.models import Counsel
from superuser_db.serializers import CounselSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status
import datetime
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def counsel_manager(request):

    if request.method == 'GET':
        counsels = Counsel.objects.all()
        counsel_id = request.query_params.get('table_id', None)
        if counsel_id is not None:
            counsels = counsels.filter(id=counsel_id)
        counsels_serializer = CounselSerializer(counsels, many=True)
        return JsonResponse(counsels_serializer.data, safe=False)

    if request.method == 'POST':
        customer_data = request.GET['customer']
        phonenum_data = request.GET['phonenum']
        email_data = request.GET['email']
        comment_data = request.GET['comment']
        counsel_date_data = datetime.datetime.now
        print(customer_data)
        print(phonenum_data)
        print(email_data)
        print(comment_data)
        counsel_obj = Counsel(
            customer=customer_data, 
            phonenum=phonenum_data, 
            email=email_data, 
            comment=comment_data,

        )
        counsel_obj.save()
        counsels = Counsel.objects.all()
        counsels_serializer = CounselSerializer(counsels, many=True)
        return JsonResponse(counsels_serializer.data, safe=False)



 

    
