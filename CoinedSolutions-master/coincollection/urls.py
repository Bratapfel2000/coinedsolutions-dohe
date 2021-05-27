from django.urls import path
from . import views

urlpatterns = [
    #path('coinhome/', views.coinhome, name='blog-home'),
    path('', views.coinhome, name='coin-home'),
    path('coinfilter/', views.coin_filter, name='coin-filter'),
    path('cointable/', views.coin_table, name='coin-table'),
    path('coinfiltertable/', views.coin_filtertable, name='coin-filtertable'),
    path('charts/', views.coin_charts, name='coin-charts'),
    path('country/<int:id>/<slug:slug>', views.country, name='country'),
    path('category/<slug:slug>/<int:id>', views.coin_detail, name='coin-detail'),

]