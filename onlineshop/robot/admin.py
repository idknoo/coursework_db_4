from django.contrib import admin
from .models import Robot, Robot_description


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    pass


@admin.register(Robot_description)
class Robot_descriptionAdmin(admin.ModelAdmin):
    pass

