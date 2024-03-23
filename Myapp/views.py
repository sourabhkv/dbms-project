from django.shortcuts import render
from mysql.connector import connect, Error
from django.http import HttpResponse

from django.shortcuts import render  
from .models import Team, Player, Umpire, Coach, Captain, Match  
from django.http import HttpResponse  
  
# Display the tables  
def tables(request):  
    teams = Team.objects.all()  
    players = Player.objects.all()  
    batsmen = players.filter(player_type='batsman')  
    bowlers = players.filter(player_type='bowler')  
    umpires = Umpire.objects.all()  
    coaches = Coach.objects.all()  
    captains = Captain.objects.all()  
    matches = Match.objects.all()  
  
    return render(request, 'show_tables.html', {  
        'teams': teams,  
        'players': players,  
        'batsmen': batsmen,  
        'bowlers': bowlers,  
        'umpires': umpires,  
        'coaches': coaches,  
        'captains': captains,  
        'matches': matches,  
    })