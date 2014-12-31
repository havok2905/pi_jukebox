class Base:

  @staticmethod
  def split_path(path):
    dirs = path.split('/')
    return filter((lambda dir: dir != '' and dir != '.' and dir != '..' ), dirs)

  @staticmethod
  def remove_root(path, pattern):
    start = len(path) - len(pattern)
    end = len(path) + 1
    return path[start:end]

  # Overwrite this method in child classes
  @staticmethod
  def valid_type():
    return True

  # Overwrite this method in child classes
  @staticmethod
  def info():
    return True
