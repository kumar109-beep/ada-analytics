# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile',views.profile,name='profile'),
    path('dashboard-filter/total-order',views.total_order_filter,name='total_order_filter'),
    path('dashboard-filter/revenue',views.revenue,name='revenue'),
    path('dashboard-filter/categrory',views.categrory,name='categrory'),

    path('dashboard-filter/categrory-filter',views.category_filter,name='category_filter'),


    path('dashboard-filter/master-filter-1',views.master_filter_1,name='master_filter_1'),
    path('dashboard-filter/master-filter-2',views.master_filter_2,name='master_filter_2'),
    path('dashboard-filter/master-filter',views.master_filter,name='master_filter'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
