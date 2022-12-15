

from django.urls import path
from AppCoder.views import * #llevar a urls mama

urlpatterns = [
    
    path("familia/", familia),
    path("familia2/", familia),
    path("familia3/", familia),

    
]