class Alien:

  def fire(self):
    print("pew pew pew")

  def explode(self):
    print("boom")

  def die(self):
    if self.points == 0:
      print("Alien died")