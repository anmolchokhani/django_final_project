import django_filters
from .models import BoxDetails


class BoxDetailsFilter(django_filters.FilterSet):
    class Meta:
        model= BoxDetails
        fields={

            'name':['contains'],
        }
           
       


