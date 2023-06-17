from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

from api.models import Agent


class AgentViewSet(viewsets.GenericViewSet):

    @action(methods=['POST'], detail=False)
    def reserve(self, request):
        """
        The reserve function is used to reserve an agent for a specific task.
        The function will return the first available agent in the database, and set its reserved status to True.


        :param self: Represent the instance of the class
        :param request: Get the request object
        :return: A message that an agent has been reserved

        """
        with transaction.atomic():
            try:
                agent = Agent.objects.filter(is_reserved=False).first()
                Agent.objects.update(id=agent.id).update(is_reserved=True)
            except Exception as e:
                raise APIException from e
            # TODO: add timer
            return Response({
                'message': f'Agent: {agent.name}({agent.id}) has been reserved'
            })

    @action(methods=['POST'], detail=False)
    def book(self, request):
        return Response
