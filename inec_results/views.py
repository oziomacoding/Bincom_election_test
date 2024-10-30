from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import AnnouncedPuResults
from .serializers import AnnouncedPuResultsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView
from .models import PollingUnit


class PollingUnitResultsView(generics.ListAPIView):
    serializer_class = AnnouncedPuResultsSerializer

    def get_queryset(self):
        unique_id = self.kwargs.get("polling_unit_uniqueid")
        return AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unique_id)


class SummedLGAResultsView(APIView):
    def get(self, request, lga_id):
        # Get the summed results for each party abbreviation in the specified LGA
        results = (
            AnnouncedPuResults.objects.filter(polling_unit_lga_id=lga_id)
            .values("party_abbreviation")
            .annotate(total_score=Sum("party_score"))
        )
        
        # Format the response data
        response_data = [{"party_abbreviation": result["party_abbreviation"], "total_score": result["total_score"]} for result in results]
        
        return Response(response_data)




class NewPollingUnitResultsView(APIView):
    def post(self, request):
        serializer = NewPollingUnitResultSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

