#Ansh patel
#9/20/24
#computer science programming one
#extra= extra question about largest empire in history
points = 0
#welcome and what quiz is about 
name=input('enter your name')
print('welcome to the game show' + name)
print('This quiz is about history')
#how to answer questions 
print('Answer using a,b,c,d')
#question 1
print('When did the roman empire fall')
empire= str(input('Is it A,1453,B,476,C 270,D 1918.'))
if empire.lower() == 'b':
    print('you are correct')
    points+=1 
    print('You got  1 point')

else:
    print('You are wrong')

#question 2    
print('who wrote the thoery of relativity')
physics=str(input('1.Oppenheimer 2.Einstein,Newton,Copernicus'))
if physics.lower()=='2':
  print('e=mc^2')
  points+=1
  print('you got points')
else: 
  print('you are wrong')


#question 3
print('When was the civil war end')
america=str(input('1.1776,2.1865,3.1900,4.2024'))
if america.lower()=='2':
    print('you are correct')
    points+=1
    print('you got points')
else:
    print('you are wrong')

#question 4
print('who founded gravity')
newton=str(input('1.newton,2.einstein,3.oppenheimer,4.lincoln'))
           
if newton.lower()=='1': 
    print('you are correct')
    points+=1
    print('you got the points')
else:
    print('you are wrong')


#question 5
print('When was the battle of 300')
sparta=str(input('1.480,2.300,3.1000,4.230'))
if sparta.lower()=='2':
    print('This is sparta')
    points+=1
    print('you got points')
else:
    print('you are wrong')
#Question 6 extra 
print('who had the largest empire in history')
britain=str(input('1.britain,2.england,3.rome,4.china'))
if britain.lower()=='1':
    print('you are correct')
    points+=1
else:
    print('you are wrong')
points = str(points)
print(points)
print('you have' +points+ 'points')

if int(points)>=3:
  print('you passed welcome to harvard')
else:
  print('you failed try again')

           
    
