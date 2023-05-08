from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Test, TestSnapshot, Mistake, Speed

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'user', 'start_time', 'end_time', 'content', 'final_wpm', 'final_accuracy', 'final_consistency', 'created_at')

class TestSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSnapshot
        fields = ('id', 'test', 'timestamp', 'wpm', 'accuracy', 'consistency', 'total_characters_typed')

class MistakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mistake
        fields = ('id', 'test', 'incorrect_char', 'correct_char', 'position')

class SpeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = ('id', 'user', 'test', 'average_wpm')
