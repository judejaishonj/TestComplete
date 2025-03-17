def checkpoint():
  Regions.OrdersView.Check(Aliases.Orders.MainForm.OrdersView)
  
def checkmyfile():
  Files.Good_morning_txt.Check("C:\\Users\\Jude Jaishon\\Documents\\Good morning2.txt")
  
def checkmyproperty():
  aqObject.CheckProperty(Aliases.Orders.OrderForm.Group.Customer, "wText", cmpEqual, "Steve Johns")