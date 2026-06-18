from django.urls import path
from .views import ai_data_entry

urlpatterns = [

    path(
        "ai-data-entry/",
        ai_data_entry,
        name="ai_data_entry"
    ),

]