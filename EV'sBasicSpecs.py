class EV():
    def __init__(self,name,company,torque,motor,performance,battery,range,charging):
        self.name = name
        self.company = company
        self.torque = torque
        self.motor = motor
        self.performance = performance
        self.battery = battery
        self.range = range
        self.charging = charging

    def message(self):
        print("""\t=====================================================
\t             EVOLVE to ELECTRIC Vehicle""")
    
    def display(self):
        print("""\t=====================================================
\t             All about '{0}' EV                      
\t-----------------------------------------------------
\t              It has Torque of {2} Nm                
\t          Electric motor power is {3} kW             
\t           Attains 0-100 km/h in {4} sec             
\t    {5} kWh of Battery with a range of {6}* km       
\t  Support fast charging from 0 % to 80 % in {7} min  
\t-----------------------------------------------------
\t           '{0}' EV brought to you by                
\t               |  '{1}' Company  |                   
\t=====================================================\n\n""".format(self.name,self.company,
self.torque,self.motor,self.performance,self.battery,self.range,self.charging))
        input("Press Enter for Main Menu ")
  
def ev_menu():
    while True:
        print("""=========================
 WELCOME to the EV world               
-------------------------
 Main Menu:""")    
        names = ['Nexon Max','Nexon Prime','Tigor','E Verito','Kona','MG ZS','Exit']
        a = 0
        while a < len(names):
            print(" {0}. {1}".format(a+1,names[a]))
            a += 1
        try:
            response = int(input("Enter your choice: "))
            if response == 1:
                obj = EV("Nexon Max","TATA",250,105,9,40.5,437,56)
            elif response == 2:
                obj = EV("Nexon Prime","TATA",245,95,9.9,30.2,312,60)
            elif response == 3:
                obj = EV("Tigor","TATA",170,55,11.2,26,306,65)      
            elif response == 4:
                obj = EV("E Verito","Mahindra",91,31,'--',20.7,110,90)
            elif response == 5:
                obj = EV("Kona","Hyundai",395,100,9.7,39.2,452,57)
            elif response == 6:
                obj = EV("MG ZS","MG",280,130,8.5,50.3,461,50)
            elif response == 7:
                break
            else:
                print("Invalid choice! Select again!")
                continue
            obj.message()
            obj.display()
        except Exception:
            print("No Input! Select again!")
ev_menu()

