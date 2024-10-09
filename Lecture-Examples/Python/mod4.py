########################## User defined functions
###### function 1

# define
def get_older(age):
  new_age = age + 1
  return new_age


dans_age = 50
# call
my_age_older = get_older(dans_age)

print(my_age_older)



###### function 2
import random

dans_playlist = ["Smells Like Teen Spirit", "Imagine", "Bohemian Rhapsody", "Hey Jude"]

# define
def play_random_song(playlist):
  song_count = len(playlist)
  song_number = random.randrange(0, song_count)

  return playlist[song_number]

# call
song1 = play_random_song(dans_playlist)
song2 = play_random_song(dans_playlist)
song3 = play_random_song(dans_playlist)

print(song1)
print(song2)
print(song3)




########################## Lambda functions
###### function 1
my_age = 50

# define
get_older = lambda age: age + 1

# call
my_age_older = get_older(my_age)

print(my_age_older)


###### function 2
# define
play_random_song = lambda playlist: playlist[random.randrange(0, len(playlist))]

# call
song1 = play_random_song(dans_playlist)
song1 = play_random_song(dans_playlist)
song1 = play_random_song(dans_playlist)

print(song1)
print(song2)
print(song3)
