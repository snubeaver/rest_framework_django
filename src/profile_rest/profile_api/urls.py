from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# register('name of api', name of viewset, base_name)
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
