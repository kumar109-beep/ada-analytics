# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import userProfile,secretKey
# Register your models here.
@admin.register(userProfile)
class userProfile(admin.ModelAdmin):
  list_display = ('id', 'userFk', 'address', 'city', 'country', 'postal_code', 'about_me')

@admin.register(secretKey)
class secretKey(admin.ModelAdmin):
  list_display = ('id', 'secret_key','timeStamp')