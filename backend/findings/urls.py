from django.urls import path, include
from .views import FindingsList

urlpatterns = [
    path('list/', FindingsList.as_view(), name='findings_list'),
]
