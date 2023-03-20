#create a house class
class House:
  #constructor method/function are called methods
  #variables in classes are attributes
  def __init__(self, area, windows, width, height, color, floors, occupied):
    self.area = area
    self.windows = windows
    self.width = width
    self.height = height
    self.color = color
    self.floors = floors
    self.occupied = occupied

  def area(width, height):
    return width * height

