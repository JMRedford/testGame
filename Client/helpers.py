def isCollided(foo, bar):
  fooCent = [foo.x + 16, foo.y + 16]
  barCent = [bar.x + 16, bar.y + 16]
  return (pow(pow(fooCent[0]-barCent[0],2)+pow(fooCent[1]-barCent[1],2),0.5) < 30)