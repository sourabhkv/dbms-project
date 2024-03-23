from django.db import models  
from django.db.models.signals import post_save  
from django.dispatch import receiver  
  
class Team(models.Model):  
    team_id = models.CharField(max_length=100, primary_key=True)  
    name = models.CharField(max_length=100)  
    ranking = models.IntegerField()  
  
class Player(models.Model):  
    player_id = models.CharField(max_length=100, primary_key=True)  
    name = models.CharField(max_length=100)  
    team = models.ForeignKey(Team, related_name="players", on_delete=models.CASCADE)  
    num_test_matches = models.IntegerField()  
    num_t20_matches = models.IntegerField()  
    num_world_cup_matches = models.IntegerField()  
    num_odis = models.IntegerField()  
    player_type = models.CharField(max_length=100, choices=[('batsman', 'Batsman'), ('bowler', 'Bowler'), ('allrounder', 'Allrounder')])  
  
    # Store statistics in JSON, or use a separate model if more complex querying is needed  
    statistics = models.JSONField(default=dict)  
  
class Umpire(models.Model):  
    umpire_id = models.CharField(max_length=100, primary_key=True)  
    name = models.CharField(max_length=100)  
    country_of_origin = models.CharField(max_length=100)  
    num_matches = models.IntegerField()  
  
class Coach(models.Model):  
    coach_id = models.CharField(max_length=100, primary_key=True)  
    name = models.CharField(max_length=100)  
    team = models.ForeignKey(Team, related_name="coaches", on_delete=models.CASCADE)  
  
class Captain(models.Model):  
    captain_id = models.CharField(max_length=100, primary_key=True)  
    player = models.OneToOneField(Player, on_delete=models.CASCADE)  
    num_years_captaincy = models.IntegerField()  
    num_wins = models.IntegerField()  
  
class Match(models.Model):  
    match_id = models.CharField(max_length=100, primary_key=True)  
    teams = models.ManyToManyField(Team)  
    stadium = models.CharField(max_length=100)  
    winner_team = models.ForeignKey(Team, related_name="won_matches", on_delete=models.SET_NULL, null=True)  
    match_date = models.DateField()  
    match_time = models.TimeField()  
    umpire = models.ForeignKey(Umpire, on_delete=models.SET_NULL, null=True)  
  
@receiver(post_save, sender=Match)  
def update_umpire_match_count(sender, instance, created, **kwargs):  
    if created and instance.umpire:  
        instance.umpire.num_matches += 1  
        instance.umpire.save()  
  
