from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Food, Package


class FoodViewSet(viewsets.GenericViewSet):

    @action(methods=['POST'], detail=False)
    def reserve(self, request):
        with transaction.atomic():
            food = Food.objects.get(name__icontains=request.data.get('name'))
            package = Package.objects.filter(is_reserved=False, food=food)
            Package.objects.update(id=package.id).update(is_reserved=True)
            # TODO: add timer
            return Response({
                'message': f'Package: {food.name}({package.id}) has been reserved'
            })

    @action(methods=['POST'], detail=False)
    def book(self, request):
        return Response
