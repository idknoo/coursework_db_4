from django.contrib import admin
from .models import Robot, Robot_description


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    # list_editable  = ['affected_animal']
    list_display =['name', 'damage_level', 'size', 'color']

    def size(self, obj):
        return obj.robot_descr.size

    def color(self, obj):
        return obj.robot_descr.color


@admin.register(Robot_description)
class Robot_descriptionAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Robot_description)

