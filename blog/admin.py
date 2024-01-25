from django.contrib import admin
from .models import Feature, LatestNews, Biz, Sen, Lorem, Category, Tranding, Image, Busin, Picture, Sit, Ipsum
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'status']
    list_filter = ['date']
    prepopulated_fields = {'slug':('name',)}