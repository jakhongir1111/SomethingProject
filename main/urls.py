from django.urls import path
from main.views import home, author, create, details, explore


urlpatterns = [
    path('', home),
    path('index.html', home),
    path('author.html', author),
    path('create.html', create),
    path('details.html', details),
    path('explore.html', explore)
]