def arithmetic_arranger(problems, calc = False):

  if len(problems) > 5 :
    return 'Error: Too many problems.'
 
  x = list()
  y = list()
  operator = list()
  output = list()
  
  l1 = str()
  l2 = str()
  l3 = str()
  l4 = str()

  
  for problem in problems:
    problem.lstrip()
    problem.rstrip()
    new_problem = problem.split(" ")
    if len(new_problem[0]) > 4 or len(new_problem[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
    if not (new_problem[1] == '+' or new_problem[1] == '-'):
      return('Error: Operator must be \'+\' or \'-\'.') 
    x.append(new_problem[0])
    operator.append(new_problem[1])
    y.append(new_problem[2])


  i = 0
  while i < len(problems):
    try:
      a = int(x[i])
      b = int(y[i])
    except:
      return('Error: Numbers must only contain digits.')
    if operator[i] == '+':
      output.append(str(a + b))
    elif operator[i] == '-':
      output.append(str(a - b))
    
    align = max(len(x[i]), len(y[i]))
    
    for n in range((align + 2) - len(x[i])):
      x[i] = ' ' + x[i]
    l1 = l1 + x[i] + '    '
    
    for n in range((align + 1)- len(y[i])):
      y[i] = ' ' + y[i]
    l2 = l2 + operator[i] + y[i] + '    '

    for n in range(align + 2):
      l3 = l3 + '-'
    l3 = l3 + '    '

    
    for n in range((align + 2) - len(output[i])):
      output[i] = ' ' + output[i]
    l4 = l4 + output[i] + '    '

    i = i + 1

  
  l1 = l1.rstrip()
  l2 = l2.rstrip()
  l3 = l3.rstrip()
  l4 = l4.rstrip()
  
  if calc == False:
    arranged_problems = l1 + '\n' + l2 + '\n' + l3
  elif calc == True:
    arranged_problems = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
  
  return arranged_problems
  
