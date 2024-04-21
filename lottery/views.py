from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status




class LotteryView(viewsets.ViewSet):
    def list(self, request):
        return Response(
            {'message': 'Hello from LotteryView!'}, 
            status=status.HTTP_200_OK)

    def create(self, request):
        return Response(
            {'message': 'Lottery created'},
            status=status.HTTP_201_CREATED)