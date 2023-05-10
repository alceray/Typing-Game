from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    @action(detail=True, methods=['get'])
    def snapshots(self, request, pk=None):
        test = self.get_object()
        snapshots = test.testsnapshot_set.all()
        serializer = TestSnapshotSerializer(snapshots, many=True)
        return Response(serializer.data)
    
