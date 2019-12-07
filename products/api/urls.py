from django.conf.urls import url
from django.urls import path

from .views import (
    ProductsAPIView,
    ProductsCreateAPIView,
    ProductsDetailAPIView,
    ProductsUpdateAPIView,
    PricesAPIView,
    ProductsDeleteAPIView,
    ProductsColorSizeAPIView,
    ProductsAddAPIView,
    )

urlpatterns = [
    url(r'^$', ProductsAPIView.as_view()),
    url(r'^create/$', ProductsCreateAPIView.as_view()),
    url(r'^add/$', ProductsAddAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', ProductsDetailAPIView.as_view()),
    url(r'^(?P<pk>\d+)/update/$', ProductsUpdateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/attributes/$', ProductsColorSizeAPIView.as_view()),
    url(r'^(?P<pk>\d+)/prices/$', PricesAPIView.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', ProductsDeleteAPIView.as_view()),

]





