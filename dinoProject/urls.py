from django.contrib import admin
from django.urls import path, include
from dinosaurs import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("dinosaurs", views.DinosaurViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
