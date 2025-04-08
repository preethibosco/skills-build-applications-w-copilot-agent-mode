from django.core.management.base import BaseCommand
from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing collections
        User.objects.delete()
        Team.objects.delete()
        Activity.objects.delete()
        Leaderboard.objects.delete()
        Workout.objects.delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor').save(),
            User(email='metalgeek@mhigh.edu', name='Tony Stark').save(),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson').save(),
            User(email='crashoverride@hmhigh.edu', name='Dade Murphy').save(),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token').save(),
        ]

        # Create teams
        Team(name='Blue Team', members=[str(user.id) for user in users[:3]]).save()
        Team(name='Gold Team', members=[str(user.id) for user in users[3:]]).save()

        # Create activities
        activities = [
            Activity(user_id=str(users[0].id), type='Cycling', duration=60, date='2025-04-08').save(),
            Activity(user_id=str(users[1].id), type='Crossfit', duration=120, date='2025-04-07').save(),
            Activity(user_id=str(users[2].id), type='Running', duration=90, date='2025-04-06').save(),
            Activity(user_id=str(users[3].id), type='Strength', duration=30, date='2025-04-05').save(),
            Activity(user_id=str(users[4].id), type='Swimming', duration=75, date='2025-04-04').save(),
        ]

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user_id=str(users[0].id), score=100).save(),
            Leaderboard(user_id=str(users[1].id), score=90).save(),
            Leaderboard(user_id=str(users[2].id), score=95).save(),
            Leaderboard(user_id=str(users[3].id), score=85).save(),
            Leaderboard(user_id=str(users[4].id), score=80).save(),
        ]

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60).save(),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120).save(),
            Workout(name='Running Training', description='Training for a marathon', duration=90).save(),
            Workout(name='Strength Training', description='Training for strength', duration=30).save(),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75).save(),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
