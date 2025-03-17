def calc():
  product_list=["Testcomplete", "python"]
  Log.Message(product_list[0])
  for product in product_list:
    Log.Message(product)
  
def mydict():
  product_dict={"Testcomplete":1000, "python":90}
  Log.Message(product_dict["Testcomplete"])
  
def exception():
  try:
    Log.Message(1/0)
  except:
    Log.Message("Can't divide by zero")
    

 

  