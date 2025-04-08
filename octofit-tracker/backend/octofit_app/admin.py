from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed admin.site.register calls for mongoengine models as they are not compatible with Django's admin interface.
