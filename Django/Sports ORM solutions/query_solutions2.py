# -----------------ForeignKey Relationships-------------------

# 1  Find all teams in the Atlantic Soccer Conference
"teams": Team.objects.filter(league__name__icontains='atlantic').filter(league__sport__icontains='soccer')

# 2  Find all (current) players on the Boston Penguins
"players": Player.objects.filter(curr_team__location__icontains='boston').filter(curr_team__team_name__icontains='penguins'),

# 3  Find all (current) players in the International Collegiate Baseball Conference


# 4  Find all (current) players in the American Conference of Amateur Football with last name "Lopez"


# 5  Find all football players


# 6  Find all teams with a (current) player named "Sophia"


# 7  Find all leagues with a (current) player named "Sophia"


# 8  Find everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
