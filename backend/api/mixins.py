# Модуль миксинов представления.
from rest_framework import mixins, viewsets


class ViewListCreateMixinsSet(
   mixins.CreateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Сет миксинов: просмотр, создание."""

    pass
 # mixins.ListModelMixin,