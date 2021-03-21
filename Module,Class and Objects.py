#Modules are like dictionaries

mystuff={'Apple':'I am Apples!'}

print(mystuff['Apple'])

#You can use modules using the . operator and also import them
#This goes in mystuff.py

def Apple():
    print('I am Apples')

tangerine="Living reflection of a dream"

import mystuff
mystuff.Apple()

#Class

class song(object):

    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_a_Song(self):
        for line in self.lyrics:
            print(line)

song1= song(["Happy bday to you",
            "Make a wish"])

song2=song(["we are the champions"])

song1.sing_a_Song()
song2.sing_a_Song()