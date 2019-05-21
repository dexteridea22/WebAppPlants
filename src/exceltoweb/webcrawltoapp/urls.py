from django.conf.urls import url

from .views import (
        PlantListView, 
      
        )

urlpatterns = [
    url(r'^$',PlantListView.as_view(), name='list'),
   
]