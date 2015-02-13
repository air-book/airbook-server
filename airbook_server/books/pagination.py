from rest_framework import pagination
from rest_framework import serializers

class CustomPaginationSerializer(pagination.PaginationSerializer):
    number = serializers.IntegerField()
    