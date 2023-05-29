from django.urls import path, include
from rest_framework import routers
from clients import views

router = routers.DefaultRouter()

router.register(r'', views.ClientsViewSet)

urlpatterns = [
    path('myclients/', views.MyClientsListView.as_view(), name='myclients'),
    path('', include(router.urls)),
]
