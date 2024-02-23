from django.urls import path
from .views import AccountViewDetail, AccountViewSet

urlpatterns = [

    path('account-view', AccountViewSet.as_view()),
    path('account-view/<int:account_id>/', AccountViewDetail.as_view())

    
]