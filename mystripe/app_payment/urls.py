from django.urls import path
from .views import ItemView, BuyView, CancelView, SuccessView

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='item'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy-item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success')
]
