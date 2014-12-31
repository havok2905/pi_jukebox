import os

class Library:

  def __init__(self, location):
    self.location = location
    self.library  = {}

  def simple_query(self, pattern):
    dirs  = os.listdir(self.location + pattern)
    files = map((lambda file: file.split('/')[-1]), dirs)
    return list(set(files))

  # "file_type" expects a class extending Base
  def query(self, pattern, file_type):
