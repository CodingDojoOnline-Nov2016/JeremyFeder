# ---------------------ManyToMany Relationships-------------------

# 1  Find all teams, past and present, that Samuel Evans has played with
"teams": Team.objects.filter(all_players__first_name__icontains='Samuel').filter(all_players__last_name__icontains='Evans')

# 2  Find all players, past and present, with the Manitoba Tiger-Cats
"players": Player.objects.filter(all_teams__location__icontains='manitoba').filter(all_teams__team_name__icontains='Tiger-Cats')

# 3  Find all players who were formerly (but aren't currently) with the Wichita Vikings
"players": Player.objects.filter(all_teams__location__icontains='Wichita').filter(all_teams__team_name__icontains='Vikings').exclude(curr_team__location__icontains='Wichita', curr_team__team_name__icontains='Vikings')

# 4  Find every team that Jacob Gray played for before he joined the Oregon Colts
"teams": Team.objects.filter(all_players__first_name__icontains='Jacob').filter(all_players__last_name__icontains='Gray').exclude(curr_players__first_name__icontains='Jacob', curr_players__last_name__icontains='Gray')

# 5  Find everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
"players": Player.objects.filter(first_name__icontains='Joshua').filter(all_teams__league__name__icontains='Atlantic Federation', all_teams__league__sport__icontains='Baseball')

# 6  Find all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
First ---  add line:      from django.db.models import Count         -  to views.py
Second --- to print result :
print 'count', Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12).count()

...and to display:

"teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12)

# 7  Show all players, sorted by the number of teams they've played for
"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
