from superuser_db.models import Counsel
from rest_framework import serializers
from rest_framework import generics
# Create your views here.


class CounselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsel
        fields = ('customer', 'counsel_date', 'phonenum', 'email', 'comment')

    