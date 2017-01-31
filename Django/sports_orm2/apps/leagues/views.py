from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):

	context = {
		# "leagues": League.objects.filter(teams__curr_players__first_name__icontains='Sophia')
		"players": Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams')
		# "teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12)
	}
	# print 'count', Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12).count()
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
