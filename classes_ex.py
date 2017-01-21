class Song(object):
    genre = "test"

    def print_song(self):
        print self.genre
        self.song = ["a", "b", "v"]
        for i in self.song:
            print i

new_song = ["Humma", "Ae Dil"]

print "Enter song1 for genre bollywood"
n = raw_input()

new_song.append(n)

print "Enter song2 bollywod genre"
n2 = raw_input()

new_song.append(n2)

new_genre = Song()

new_genre.print_song()






