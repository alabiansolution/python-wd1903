# 0 – 34 = Fail
# 35 – 44 = Pass
# 45 – 49 = Fair
# 50 – 59 = Good
# 60 – 69 = Very Good
# 70 – 100 = Excellence
score = -0.8
if score >=0 and score < 35:
	grade = 'F'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
elif score >=35 and score < 45:
	grade = 'P'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
elif score >=45 and score < 50:
	grade = 'Fair'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
elif score >=50 and score < 60:
	grade = 'Good'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
elif score >=60 and score < 70:
	grade = 'Very Good'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
elif score >=70 and score <= 100:
	grade = 'Excellent'
	result = 'Your score is '+str(score)+' and your grade is '+grade
	print(result)
else:
	print('invalid score')
