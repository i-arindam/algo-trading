"""algo_trading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    # Instrument
    path("instruments/show/<int:pk>", views.instrument_by_pk, name="instrument"),
    path(
        "instruments/show/<str:symbol>",
        views.instrument_by_symbol,
        name="instrument-symbol",
    ),
    path("instruments/add", views.add_instruments, name="add-instrument"),
    path("instruments", views.list_instruments, name="list-instruments"),
    # Zerodha
    path("zerodha_login_url", views.zerodha_login_url, name="zerodha-login-url"),
    path("zerodha_req_token", views.zerodha_req_token, name="zerodha-req-token"),
    path("zerodha_instruments", views.zerodha_instruments),
    # Trading System
    path(
        "trading_system/place_options_call",
        views.place_options_call,
        name="place-options-call",
    ),
    path("trading_system/calls/<int:pk>", views.trading_signal, name="trading-signal"),
    path("trading_system/calls/options", views.options_calls, name="options-calls"),
]

# Additional URLs from other apps
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
