from django.contrib import admin
from .models import Animal, Location, Health_description


@admin.register(Animal)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['animal_name', 'specie', 'health', 'located_in', 'age']

    def located_in(self, obj):
        return obj.location.location_name

    def health_description(self, obj):
        return obj.health_description.health_description

@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    pass

@admin.register(Health_description)
class Health_descriptionAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Health_description)
admin.site.unregister(Location)

