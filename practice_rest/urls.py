from django.urls import path
from .views import practiceRest, snippet_detail, snippet_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', practiceRest),
    path('list/' , snippet_list),
    path('detail/<int:pk>/' , snippet_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)