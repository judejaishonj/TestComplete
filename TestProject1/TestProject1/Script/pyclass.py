class Dog:
  def __init__(self,name,color):
    Log.Message("Constructor")
    self.name = name 
    self.color = color
    
def test():
  mydog = Dog("puppy","white")
  Log.Message(mydog.name)
  Log.Message(mydog.color)