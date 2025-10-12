from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet, HouseViewSet, AgencieViewSet, InvestorViewSet, BankViewSet

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'apartments', ApartmentViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'agencies', AgencieViewSet)
router.register(r'investors', InvestorViewSet)
router.register(r'banks', BankViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version='v1',
        description="Swagger dokumentacija za Real Estate projekat",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
