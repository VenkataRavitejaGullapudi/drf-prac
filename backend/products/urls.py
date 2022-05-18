from django.urls import path

from . import views

urlpatterns = [
    path("detail/<int:pk>/",views.ProductDetailAPIView.as_view()),
    path("",views.ProductCreateAPIView.as_view())
]
