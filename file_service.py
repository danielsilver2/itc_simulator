class File:
  def createResultFileWith(txt):
    f = open("outcoming_result.txt", "w+")
    f.write(txt)
    f.close()

  def createOutcomingFileWith(txt):
    f = open("outcoming.txt", "w+")
    f.write(txt)
    f.close()

  def readFile():
      f = open("incoming.json", "r")
      return f.read()
