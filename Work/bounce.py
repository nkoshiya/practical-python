# bounce.py
## program excercise 1.5 Bouncing Ball
#bounce.py

wall_height = 100 # meters
bounce_no = 0
frac = 3/5

while bounce_no < 10:
    bounce_no += 1
    bounce_height = (frac**bounce_no) * wall_height
    print(f'{bounce_no} {round(bounce_height,4)}')
    
# Exercise 1.5
