from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class FoodViewSet(viewsets.GenericViewSet):

    @action(methods=['POST'], detail=False)
    def reserve(self, request):
        return Response()

    @action(methods=['POST'], detail=False)
    def book(self, request):
        return Response
