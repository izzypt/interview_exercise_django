from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from findings.models import FindingsModel, ScanModel
from .serializers import FindingsSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
#class MyPagination(PageNumberPagination):
#    page_size = 3

class FindingsList(APIView):
    def get(self, request, format=None):
        # Get query parameters if any
        definition_id = request.GET.get('definition_id')
        scan_value = request.GET.get('scan_value')
        
        # Get all findings
        findings = FindingsModel.objects.all()
        if definition_id:
            findings = findings.filter(definition_id=definition_id)
        if scan_value:
            findings = findings.filter(scans__value=scan_value)

        # Serialize findings and respond
        serializer = FindingsSerializer(findings, many=True)
        findings_count = len(serializer.data)
        if findings_count == 0:
            return Response({'Message' : 'No content found'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'count': findings_count, 'results': serializer.data}, status=status.HTTP_200_OK)