import re
from base import Base

class Music(Base):

  def __init__(self, path):
    pattern = ['artist', 'album', 'song']

    path_list = Base.split_path(path)
    path_list = Base.remove_root(path_list, pattern)

    self.path      = path
    self.path_list = path_list
    self.pattern   = pattern
    self.artist    = path_list[0]
    self.album     = path_list[1]
    self.song      = path_list[2]

  def valid_type(self):
    if re.match(r'([^\s]+(\.(?i)(mp3|mp4|m4p|m4a))$)', self.path):
      return True
    else:
      return False

  def name(self):
    return re.sub(r'[.mp3, .mp4, .m4p, .m4a]', '', self.song)

  def info(self):
    return [self.artist, self.album, self.song, self.path]
