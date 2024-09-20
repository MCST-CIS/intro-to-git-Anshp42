#Ansh patel
#9/20/24
#computer science programming one
#extra= extra questions
points = 0
name=input('enter your name')
print('welcome to the game show' + name)
print('This quiz is about history')
print('Answer using a,b,c,d')
print('When did the roman empire fall')
empire= str(input('Is it A,1453,B,476,C 270,D 1918.'))
if empire.lower() == 'b':
    print('you are correct')
    points+=1 
    print('You got points')

else:
    print('You are wrong')
    
