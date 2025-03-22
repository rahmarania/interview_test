# classify the exam result
exam = [65,80,76]

def classify_exam(exam):
  avg = sum(exam)/len(exam)

  if avg <= 68:
    return 'Sorry, you need to take the exam next year'
  else:
    return 'You Passed!'
  
