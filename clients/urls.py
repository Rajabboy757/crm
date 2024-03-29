from django.urls import path, include
from rest_framework import routers
from clients import views

router = routers.DefaultRouter()

router.register(r'', views.ClientsViewSet)

urlpatterns = [
    path('send_emails', views.SendingEmailsAPIView.as_view(), name='send_emails_to_company_clients'),
    path('', include(router.urls)),
]
