from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

from api.models import Food, Package


class FoodViewSet(viewsets.GenericViewSet):

    @action(methods=['POST'], detail=False)
    def reserve(self, request):
        """
        The reserve function is used to reserve a package of food.
            The function takes in the name of the food and returns a message that says
            &quot;Package: {food_name}({package_id}) has been reserved&quot; if successful.

        :param self: Represent the instance of a class
        :param request: Get the data from the request
        :return: A message that the package has been reserved
        """
        with transaction.atomic():
            try:
                food = Food.objects.get(name__icontains=request.data.get('name'))
                package = Package.objects.filter(is_reserved=False, food=food)
                Package.objects.update(id=package.id).update(is_reserved=True)
            except Exception as e:
                raise APIException from e
            # TODO: add timer
            return Response({
                'message': f'Package: {food.name}({package.id}) has been reserved'
            })

    @action(methods=['POST'], detail=False)
    def book(self, request):
        return Response
