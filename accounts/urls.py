from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('sing/', SignUpView.as_view(),name='signup'),
]