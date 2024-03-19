from random import randint
from random import randrange
from tabulate import tabulate

# Overhead Variables
SECONDS_PER_ITEM = 4
OVERHEAD_SECONDS = 30
ADDITIONAL_TIME = 45
range_reps = 500

# Create Queue class
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []    
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)    
    def display(self):
        return(self.items)    
    def index(self, index):
        return self.items[index]    
    def index_change(self, index, num):
        self.items[index] = num
        return num

# Define class for Customer
class Customer:
    def __init__(self,time):
        self.items = randint(6,20)  
        self.timeStamp = time
        self.time_at_reg = (SECONDS_PER_ITEM*self.items + ADDITIONAL_TIME)
        self.cust_wait_time = 0
    def get_items(self):
        return self.items
    def get_stamp(self):
        return self.timeStamp
    def wait_time(self,currentTime):
        return currentTime - self.timestamp

            
# Define class for Registers
class Register:
    def __init__(self):
        self.cust_served = 0
        self.items_served = 0 
        self.idle_time = 0 
        self.currentCust = None
        self.cust_wait = 0 
        self.q = Queue()
        self.time = Queue()
    def idle(self):
        return self.currentCust == None
    def NextCust(self,items):
        self.cust_served += 1
        self.items_served += items
    def Enqueue(self,item):
        self.q.enqueue(item)
    def Dequeue(self):
        self.q.dequeue()
    def size(self):
        return self.q.size()
    def display(self):
        return(self.q.display())
    def isEmpty(self):
        return self.q.isEmpty()
    def Enqueue_time(self,item):
        self.time.enqueue(item)
    def Dequeue_time(self):
        self.time.dequeue()
    def size_time(self):
        return self.time.size()
    def display_time(self):
        return self.time.display()
    def isEmpty_time(self):
        return self.time.isEmpty()
    
    
    
# Function for when a new customer is created    
def new_customer():
    return randrange(30) == 0


# Chooses the line with least customers or express
def line_choice(regList,customer):
    if customer.get_items() <= 10:
        selected_line = regList[0]
        for lineChoice in regList:
            if selected_line.size() > lineChoice.size():
                selected_line = lineChoice
        return selected_line
    else: 
        regList.pop(0)
        selected_line = regList[0]
        for lineChoice in regList:
            if selected_line.size() > lineChoice.size():
                selected_line = lineChoice
        return selected_line



# Dequeues customer when they are through the line
def checkout(i):
    if not i.isEmpty_time():
        if i.time.index(-1) == 0:
            items = i.q.dequeue()
            i.time.dequeue()
            i.cust_served += 1
            return items
        else:
            return 0
                

# Runs the logged times through each second to push customers through the line
def tick(i):
    if not i.isEmpty_time():
        if i.time.index(-1)  != 0:
            i.time.index_change(-1, (i.time.index(-1) - 1))


# Create table to print every 50 seconds                
def create_table(reg_list,currentSecond):
    print(f"time={currentSecond}\nreg#    customers")
    for i in range(len(reg_list)): 
        print(f"{i}. {reg_list[i].display()}")
    print("\n")
    
      
# Runs the 2 hours simulation block   
def simulation(simlength):
    reg1 = Register()
    reg2 = Register()
    reg3 = Register()
    reg4 = Register()
    regEx = Register()
    # All the calculations performed for every passing second
    for currentSecond in range(simlength):
        reg_list = [regEx, reg1, reg2, reg3, reg4]
        if new_customer():
            next_customer = Customer(currentSecond)
            da_line = line_choice(reg_list,next_customer)
            da_line.Enqueue(next_customer.get_items())
            da_line.Enqueue_time(next_customer.time_at_reg)
        for i in reg_list:
            tick(i)
            if i.isEmpty():
                i.idle_time += 1
            if i.q.size() >= 2: 
                i.cust_wait += 1
            try:
                i.items_served += checkout(i)
            finally: 
                continue
        # Prints the table every 50 seconds
        if currentSecond % 50 == 0:
            create_table(reg_list,currentSecond)
    # Table printed at the end
    data = [[1,reg1.cust_served,reg1.items_served,reg1.idle_time/60],
            [2,reg2.cust_served,reg2.items_served,reg2.idle_time/60],
            [3,reg3.cust_served,reg3.items_served,reg3.idle_time/60],
            [4,reg4.cust_served,reg4.items_served,reg4.idle_time/60],
            ['Express',regEx.cust_served,regEx.items_served,regEx.idle_time/60]]
    headers = ['Register','Total Customers', 'Total Items', 'total idle time (mins)']
    table = tabulate(data,headers)
    print(table)


    
def main():    
    for i in range(12):
        simulation(7200)
       
        
       
main()
        
        
        
    