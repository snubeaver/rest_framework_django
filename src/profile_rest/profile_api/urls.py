from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# register('name of api', name of viewset, base_name)
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # 모델 루터는 base_name 자동으로 생성


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
