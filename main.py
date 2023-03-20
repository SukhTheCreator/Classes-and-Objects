#create a house class
class House:
  #constructor method/function are called methods
  #variables in classes are attributes
  def __init__(self, windows, width, height, color, floors, occupied):
    # self.area = area
    self.windows = windows
    self.width = width
    self.height = height
    self.color = color
    self.floors = floors
    self.occupied = occupied

  def area(self, width, height):
    return width * height

redHouse = House (3, 15, 20, "red", 2, True)
print(redHouse.area(34, 25))

blueHouse = House (5, 36, 30, "blue", 4, True)
print(blueHouse.area(40, 32))

greyHouse = House (4, 26, 40, "grey", 2, True)
print(greyHouse.area(25, 30))