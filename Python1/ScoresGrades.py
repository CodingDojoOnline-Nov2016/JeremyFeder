print "Scores and Grades"
def score_grade():
    count = 1
    while count <= 10:
        print "Please enter your score."
        try:
            score = int(raw_input())
        except:
            print "NOPE!"
            score = 0
        if score < 60 or score > 100:
            print "Please enter a score between 60 and 100"
        elif score < 70:
            print "Score:", score,";","Your grade is D"
            count += 1
        elif score < 80:
            print "Score:", score,";","Your grade is C"
            count += 1
        elif score < 90:
            print "Score:", score,";","Your grade is B"
            count += 1
        else:
            print "Score:", score,";","Your grade is A"
            count += 1
score_grade()
print "End of program. Bye!"
