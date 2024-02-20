from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Cat
from .serializers import CatSerializer


class CatViewSets(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(['get'], False)
    def get_cat_breed(self, request):
        data = self.queryset.first().get_cat_breed()
        return Response(data, content_type='application/json')

    @action(['get'], False)
    def get_cat_color(self, request):
        data = self.queryset.first().get_cat_color()
        return Response(data, content_type='application/json')
