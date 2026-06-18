from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),

    path("", include("accounts.urls")),

    path("", include("dashboard.urls")),

    path("", include("employees.urls")),

    path("", include("chatbot.urls")),

    path("", include("leaves.urls")),

    path("", include("reports.urls")),
    
    path("",include("ai_assistant.urls")),

    path("",include("departments.urls")),

    path("", include("attendance.urls")),


]