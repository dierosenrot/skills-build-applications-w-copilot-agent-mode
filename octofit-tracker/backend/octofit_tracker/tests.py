from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        self.batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)

    def test_user_team(self):
        self.assertEqual(self.ironman.team.name, 'Marvel')
        self.assertEqual(self.batman.team.name, 'DC')

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.ironman, type='run', duration=30, distance=5)
        self.assertEqual(activity.user.username, 'ironman')

    def test_workout_creation(self):
        marvel = Team.objects.get(name='Marvel')
        workout = Workout.objects.create(name='Hero HIIT', description='HIIT for heroes', suggested_for=marvel)
        self.assertEqual(workout.suggested_for.name, 'Marvel')

    def test_leaderboard(self):
        Leaderboard.objects.create(user=self.ironman, score=100)
        self.assertEqual(Leaderboard.objects.get(user=self.ironman).score, 100)
