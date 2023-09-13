class Bankaccount:
  def __init__(self, acc_num,acc_holder_name,initial_bal=0.0):
    self.__acc_num = acc_num
    self.__acc_holder_name = acc_holder_name
    self.__acc_bal= initial_bal
  def deposit(self,amount):
    if amount > 0:
      self.__acc_bal += amount
      print("Deposit ${}.New balance:${}".format(amount,self.__acc_bal))
    else:
      print("Invalid deposit amount. Please deposit a positive amount. ")
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__acc_bal:
      self.__acc_bal -= amount
      print("Withdraw $",amount,"New balance $",self.__acc_bal)
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def disp_bal(self):
    print("Account balance for {} (Account #{}):${} ".format(self.__acc_holder_name,
    self.__acc_num, self.__acc_bal))
account= Bankaccount(acc_num = "123456789",
                    acc_holder_name = "Anandhi",
                    initial_bal = 7000.0 )
account.disp_bal()
account.deposit(300.0)
account.withdraw (500.0)
account.disp_bal()

      
      