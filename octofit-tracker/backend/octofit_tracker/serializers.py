from rest_framework import serializers

# Define serializers for the collections
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField())

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
