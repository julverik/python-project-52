from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from users.views import CustomLoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("users/", include("users.urls")),
    path("statuses/", include("statuses.urls")),
    path("labels/", include("labels.urls")),
    path("tasks/", include("tasks.urls")),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
