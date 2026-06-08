from rest_framework import mixins, viewsets

from .models import Image, News, NewsMaterial
from .serializers import NewsImageSerializer, NewsMaterialSerializer, NewsSerializer


class NewsMaterialViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = NewsMaterial.objects.select_related("category_territory").all()
    serializer_class = NewsMaterialSerializer


class NewsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = News.objects.select_related(
        "news_material",
        "category_territory",
    ).all()
    serializer_class = NewsSerializer


class NewsImageViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Image.objects.select_related("news").all()
    serializer_class = NewsImageSerializer
