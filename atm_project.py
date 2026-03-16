class Atm:
  def __init__(self):
    self.pin=''
    self.balance= 0
    self.d={
        "sai":12736754,
        "ramu":673653,
        "dhanu":67677612,
        "kasi":873783
    }
    self.menu()

#we have created our attributes in constructor
  def menu(self):
    print(""" 1) Press 1 to create pin.
    2)press 2 to cash withdrawal.
    3)press 3 to cash deposit.
    4)press 4 to cash transfer.
    5)press 5 to change pin.
    6)press 6 to check balance.
    7)press 7 to exit""")
    user=input("enter the option:")
    if user=='1':
       self.create_pin()
    elif user=='2':
      self.cash_withdrawal()
    elif user=='3':
      self.cash_deposit()
    elif user=='4':
      self.cash_transfer()
    elif user=='5':
      self.change_pin()
    elif user=='6':
      self.check_balance()
    elif user=='7':
      exit()
    else:
      print("invalid option")
  def create_pin(self):
      ask1=input("enter the pin:")
      self.pin=ask1

      bal=int(input("enter the balance:"))
      self.balance=bal
      print("pin created successfully")
      self.menu()


  def cash_withdrawal(self):
    ask2=input("enter the pin:")
    if ask2==self.pin:
      ask3=int(input("enter the amount u want to withdraw:"))
      if ask3 > self.balance:
        print("insufficient balance")
      else:
        self.balance=self.balance-ask3
        print("please collect ur ",ask3,"₹","you account balance is left with ",self.balance,"₹")
    else:
      print("invalid pin")
    self.menu()
  def cash_deposit(self):         #cash deposit
    ask4=input("enter the pin:")
    if ask4==self.pin:
      ask5=int(input("enter the amount u want to deposit ₹ :"))
      self.balance=self.balance+ask5
      print("ur account balance is left with ",self.balance,"₹")
    else:
      print("invalid pin")
    self.menu()
  def change_pin(self):        #check balance
    ask6=input("enter the pin:")
    if ask6==self.pin:
      ask7=input("enter the new pin:")
      self.pin=ask7
      print("pin has been changed succesfully")
    else:
      print("invalid pin")
    self.menu()
  def cash_transfer(self):         #transfer the amount to another
    ask8=input("enter the pin:")
    if ask8==self.pin:
      ask9=input("enter the name of the person u want to transfer:")
      for i in self.d:
       if ask9 in i:
          ask10=int(input("enter the account no:"))
          if ask10 == self.d[ask9]:
            ask11=int(input("enter the amount u want to transfer:"))
            if ask11 > self.balance:
               print("insufficient balance")
            else:
               self.balance=self.balance-ask11
               print("please collect ur ",ask11,"₹","you account balance is left with ",self.balance,"₹")
               print("amount ", ask11, "has been transeferd to ", ask10)
  def check_balance(self):
    ask12=input("enter the pin:")
    if ask12==self.pin:
      print("ur account balance is left with ",self.balance,"₹")
    else:
      print("invalid pin")
      
sbi_user=Atm()
