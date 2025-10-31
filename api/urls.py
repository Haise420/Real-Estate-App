from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet, HouseViewSet, AgencyViewSet, InvestorViewSet, BankViewSet, ClientViewSet, ConversationListView, ConversationDetailView, SendMessageView  
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'houses', HouseViewSet)
router.register(r'agencies', AgencyViewSet)
router.register(r'investors', InvestorViewSet)
router.register(r'banks', BankViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Real Estate API",
        default_version='v1.1',
        description="Swagger dokumentacija za Real Estate projekat",
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/register/', RegisterView.as_view(), name='rest_register'),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('conversations/<int:pk>/', ConversationDetailView.as_view(), name='conversation-detail'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
]
