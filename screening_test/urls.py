from django.contrib import admin
from django.urls import path, include
from mozilla_django_oidc import views as oidc_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "oidc/authenticate/",
        oidc_views.OIDCAuthenticationRequestView.as_view(),
        name="oidc_authentication_init",
    ),
    path(
        "oidc/callback/",
        oidc_views.OIDCAuthenticationCallbackView.as_view(),
        name="oidc_authentication_callback",
    ),
    path("api/v1/sales/", include("apps.sales.urls"), name="sales"),
]


admin.site.site_header = "Savanah Admin"
admin.site.site_title = "Savanah Admin Portal"
admin.site.index_title = "Welcome to the Savanah Portal"
