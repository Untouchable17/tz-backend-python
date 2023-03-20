from django.urls import path

from src.menu import views


app_name = "menu_app"

urlpatterns = [
    path("", views.IndexViewPage.as_view(), name="index_url"),
    path("<int:pk>", views.IndexViewPage.as_view(), name="category_detail")
]
