import csv

class Client():

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def Show_details(self):
        print(f'Client Details')
        print("")
        print(f"Name : - {self.name}")
        print(f"Balance : - {self.balance}")

    def Names(name):
        return name
    def Balances(balance):
        return balance


class Transaction(Client):



    def __init__(self,name,balance):
        self.balance=balance
        self.name = name


    def Deposit(self,amount): 
        #self.amount = amount
        self.balance = amount + self.balance
        #return(f'Account balance for {self.name} has been deposit and bal is  {self.balance}')

        return self.balance

    def Withdraw(self,amount):
        #self.amount = amount
        if amount > self.balance:
            return(f'Insufficient balance to withdraw: Your bal is:  {self.balance}')
        else:
            self.balance = self.balance - amount
            return self.balance

    def Transfer(self,other,amount_out):
        if not self.balance<amount_out:
            self.Withdraw(amount_out)
            other.Deposit(amount_out)


    def View_Balances(self):
        self.Show_details()
        return(f'Account balanc : {self.balance}')

all_clients=[]
uniq=[]
new_list = []

with open('edited.csv', 'r')as my_file:
        reader = csv.reader(my_file, delimiter=",")
        for row in reader:
            all_clients.append(row[1])
            for i in all_clients:
                uniq.append(i)
                if i not in uniq:
                    uniq.append(i)
                    print(i)
                    new_list.append(Client(i,100))
                    print(new_list)




Charles = Transaction("Charles",1000)
ken = Transaction('ken',250)

ken.Withdraw(100)

Charles.Transfer(ken,10)
print(ken.Show_details())
print(Charles.Show_details())

# for i in uniq:
#     c= Client(i,100)
#     print(c)


# obj_list = []
# for i in range(len(uniq)):
    
#     # print(uniq)
#     print(i)
#     obj_list[i][0].append(Client(i,100))
#     print(obj_list[i].balance())






