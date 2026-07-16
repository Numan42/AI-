# OPP concept
class Person:
    def __init__(self, user_name, email, pasoword, address):
        self.user_name = user_name
        self.email = email
        self.password = pasoword
        self.Address = address
        
    def greet(self):
        print(f"{self.user_name} welcome")
    
    def person_address(self):
        print(f"address of {self.user_name} is {self.Address}")
    

person_1 = Person("numan","itsnuman@gmail.com",111111,"west london")
        
# person_1.greet()
# person_1.person_address()


class Song:
    def __init__(self, name):
        self.name = name
        self.song = []
    
    def add_song(self, song):
        self.song.append(song)
    
    def remove_song(self, song):
        self.song.append(song)
    
    def show_songs(self):
        print(f"platlist'{self.song}'")
        for songs in self.song:
            print(songs)

my_playlist = Song("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()