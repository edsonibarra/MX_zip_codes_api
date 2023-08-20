from django.urls import path
from .views import CodesView

urlpatterns = [
    path('zipCodes/<str:zip_code>/', CodesView.as_view()),
]