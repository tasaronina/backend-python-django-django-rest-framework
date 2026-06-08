from django.contrib import admin

from .models import CategoryTerritory, Image, News, NewsMaterial


admin.site.register(CategoryTerritory)
admin.site.register(NewsMaterial)
admin.site.register(News)
admin.site.register(Image)
