from file.library import Library
from file.music import Music

class Jukebox(Library):

  def artist_init(self, artist):
    if artist not in self.library:
      self.library[artist] = {}

  def album_init(self, artist, album):
    if album not in self.library[artist]:
      self.library[artist][album] = { songs: [] }

  def song_init(self, artist, album, song, file):
    self.library[artist][album][:songs].append({ name: song, path: file })

  def collect_music(self):
    for file in os.listdir(self.location + '*/*/*'):
      song = Music(file)
      if song.valid_type():
        artist_init(song.artist)
        album_init(song.artist, song.album)
        song_init(*song.info)

    return self.library

  def artists(self):
    return simple_query('/*')

  def artist_albums(self, artist):
    return simple_query('/' + artist + '/*')

  def album_songs(self, artist, album):
    return query('/' + artist '/' + album + '/*', Music)

  def artist_songs(self, artist):
    return query('/' + artist + '/*/*', Music)
