from rest_framework import viewsets
from rest_framework.response import Response
from todos.models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class= TodoSerializer

    def get_queryset(self):
        todos= Todo.objects.all()
        return todos



    def retrieve(self, request, *args, **kwargs):
        params= kwargs['pk'].split('=')[1]
        #print(params)
        todos= Todo.objects.all()[:int(params)]
        serializer= TodoSerializer(todos, many=True)
        return Response(serializer.data)