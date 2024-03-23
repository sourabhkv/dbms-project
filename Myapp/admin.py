from django.contrib import admin  
from .models import Team, Player, Umpire, Coach, Captain, Match  
  
# Register your models here.  
admin.site.register(Team)  
admin.site.register(Player)  
admin.site.register(Umpire)  
admin.site.register(Coach)  
admin.site.register(Captain)  
admin.site.register(Match)  
