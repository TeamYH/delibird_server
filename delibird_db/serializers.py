from delibird_db.models import Table
from rest_framework import serializers
from rest_framework import generics
# Create your views here.


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'pos_x', 'pos_y', 'angle')

    