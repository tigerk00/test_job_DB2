from django.urls import path
from .views import MessageList, MessageDetail, MessageCreate

app_name = "chat"
urlpatterns = [
    path('single/<int:pk>/', MessageDetail.as_view(), name="api_detail_page"),
    path('list/', MessageList.as_view(), name="api_list_page"),
    path('create/', MessageCreate.as_view(), name="api_create_page"),
]