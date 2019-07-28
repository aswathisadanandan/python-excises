class Car:
  def __init__(self,milage):
    self.Milage=milage
    print("Hai")
  def SetType(self,type):
    self._Type=type
  def GetType(self):
    return self._Type

  def SetModel(self,model):
    self._Model=model
  def GetModel(self):
    return self._Model

  def SetPrice(self,*args,**kwargs):
    print(kwargs)
    print(args)
  def GetPrice(self):
    return self._Price

  def SetMilesDrive(self,milesDrive):
    self._MilesDrive=milesDrive
  def GetMilesDrive(self):
    return self._MilesDrive

  def SetOwner(self,owner):
    self._Owner=owner
  def GetOwner(self):
    return self._Owner
  def GetCurrentPrice(self):
    self._price=(self._MilesDrive*self.Milage)
    return self._price

def main():
  myCar=Car(20)
  myCar.SetType("BMW")
  myCar.SetModel(2017)
  myCar.SetPrice(28000,{2:4},Price=28999)
  #myCar.SetMilesDrive(15)
  #myCar.SetOwner("Adarsh")
 # CurrentPrice=myCar.GetCurrentPrice()
  #print("New Price {}".format(CurrentPrice))
if __name__=='__main__':main()
