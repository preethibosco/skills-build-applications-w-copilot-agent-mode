from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from octofit_app.models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    codespace_url = "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
    return Response({
        'users': f'{codespace_url}/api/users/',
        'teams': f'{codespace_url}/api/teams/',
        'activity': f'{codespace_url}/api/activity/',
        'leaderboard': f'{codespace_url}/api/leaderboard/',
        'workouts': f'{codespace_url}/api/workouts/',
    })

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class ActivityList(APIView):
    def get(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardList(APIView):
    def get(self, request):
        leaderboard = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

class WorkoutList(APIView):
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)