while True:
    class E_Bill():
        print("\n\t*******Welcome to E-Bill Portal*******\n")
        def __init__(self,reading):
            self.reading = reading
        def message(self):
            print("\n\t************E-Bill Receipt************")
        def calculation(self):
            try:
                self.reading = int(self.reading)
                if self.reading >= 0 and self.reading <= 50:
                    cost = 0
                    print("""\t======================================
\t Congrats!, You got free Electricity.""")
                elif self.reading>50 and self.reading<=100:
                    units = self.reading-50
                    cost = units*8.8
                elif self.reading>100 and self.reading<=200:
                    units = self.reading-50
                    cost = units*10
                elif self.reading>200 and self.reading<=300:
                    units = self.reading-50
                    cost = units*12
                elif self.reading>300 and self.reading<=400:
                    units = self.reading-50
                    cost = units*14
                elif self.reading>400:
                    units = self.reading-50
                    cost = units*16   
                else:
                    print("\t Incorrect Reading!")
                print("""\t======================================
\t Energy meter reading is {0} and
\t Electricity bill is: Rs. {1:.2f}/-
\t======================================""".format(self.reading,cost))
            except Exception:
                print("""\t======================================
\t\t    !Try Again!
\t '{0}' is an invalid reading.
\t Please enter a valid reading.
\t======================================""".format(self.reading))
            finally:
                print("""\t  Thank You for using E-Bill Portal.
\t**************************************\n""")
                print(" Press 'Enter' to continue ")
                input()       

    bill = E_Bill(input("Enter energy meter reading: "))
    bill.message()
    bill.calculation()
