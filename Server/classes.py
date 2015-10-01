class QuadTree:
  def __init__(self, levels, xStart, xEnd, yStart, yEnd, parentTree = None):
    self.children = [None,None,None,None]  #nw,ne,sw,se
    self.parentTree = parentTree
    self.xBounds = [xStart,xEnd]
    self.yBounds = [yStart,yEnd]
    self.things = []
    if (levels > 1):
      self.isLeaf = False
      self.children[0] = QuadTree(levels - 1, xStart, (xEnd+xStart)/2, yStart, (yEnd+yStart)/2, self)
      self.children[1] = QuadTree(levels - 1, (xEnd+xStart)/2, xEnd, yStart,(yEnd+yStart)/2, self)
      self.children[2] = QuadTree(levels - 1, xStart, (xEnd+xStart)/2, (yEnd+yStart)/2, yEnd, self)
      self.children[3] = QuadTree(levels - 1, (xEnd+xStart)/2, xEnd, (yEnd+yStart)/2, yEnd, self)
    else:
      self.isLeaf = True

    def contains(self, thing):
      return (self.xBounds[0] <= thing.x and self.xBounds[1] > thing.x and self.yBounds[0] <= thing.y and self.yBounds[1] > thing.y)

    def insert(self, thing):
      if (self.isLeaf):
        self.things.push(thing)
      else:
        for child in children:
          if child.contains(thing):
            child.insert(thing)

class Entity:
  pass

class Player(Entity):
  pass

class Enemy(Entity):
  pass

class Static(Entity):
  pass

class Projectile(Entity):
  pass