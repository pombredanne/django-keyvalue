from django.contrib import admin

from models import Store


class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ("key", )

admin.site.register(Store, StoreAdmin)
