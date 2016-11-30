print "Scores and Grades"
def score_grade(score):
    for count in range (0, 10, 1):
        if score >= 60 and score <= 69:
            print "Score:", score,";","Your grade is D"
            count += 1
        elif score >= 70 and score <= 79:
            print "Score:", score,";","Your grade is C"
            count += 1
        elif score >= 80 and score <= 89:
            print "Score:", score,";","Your grade is B"
            count += 1
        elif score >= 90 and score <= 100:
            print "Score:", score,";","Your grade is A"
            count += 1
        else:
            print "Please enter a score between 60 and 100"
score_grade(77)
print "End of program. Bye!"
# Could not figure out how to make a seperate prompt per iteration. Best semi-working version I could come up with :-?
