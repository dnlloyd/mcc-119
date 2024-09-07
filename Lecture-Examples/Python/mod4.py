import random

dans_playlist = ["Smells Like Teen Spirit", "Imagine", "Bohemian Rhapsody", "Hey Jude"]

def play_random_song(playlist):
  song_count = len(playlist)
  song_number = random.randrange(0, song_count)

  return playlist[song_number]

song1 = play_random_song(dans_playlist)
song2 = play_random_song(dans_playlist)
song3 = play_random_song(dans_playlist)

print(song1, song2, song3)



########################## 4.4
# User defined function
my_age = 50

def get_older(age):
  age += 1
  return age

my_age_older = get_older(my_age)
print(my_age_older)


# Lambda function
my_age = 50

get_older = lambda age: age + 1
my_age_older = get_older(my_age)
print(my_age_older)



########################## 4.4

