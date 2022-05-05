from argparse import Namespace
from django.urls import path, include
from .viewsets import *
from .router import *
from rest_framework.urlpatterns import format_suffix_patterns


# app_name = 'pro_api'
urlpatterns = [

    # Entrypoint/Root (Endpoint) for api
    path('', include(default_router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
