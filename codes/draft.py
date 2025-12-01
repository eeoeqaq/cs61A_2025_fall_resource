# write any code you want
from karel.stanfordkarel import *

def main():
   if front_is_blocked():
      return 0
   move()
   if front_is_blocked():
      return 0
   move()
   main()
   turn_left()
   turn_left()
   move()
  