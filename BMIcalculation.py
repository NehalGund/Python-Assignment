# Body Mass Index Calculator
def bmi_calc():
    while True:
        try:
            print("\t******Body Mass Index*******")
            while True:
                print("\n\tSelect Weight Unit:")
                weight = ['Kilograms','Pounds','Exit Program']
                a = 0
                while a < len(weight):
                    print("\t {0}. {1}".format(a+1,weight[a]))
                    a += 1
                response1 = int(input("\tEnter choice number: "))
                if response1 == 1:
                    kg = float(input("\tEnter weight in kg: "))
                    wt = kg
                elif response1 == 2:
                    lbs = float(input("\tEnter weight in lb: "))
                    wt = lbs / 2.205
                elif response1 == 3:
                    exit()
                elif response1 <= 0 or response1 > len(weight):
                    print("\t*******************************\n\tIncorrect Choice! Select Again!")
                    continue
                while True:
                    print("\n\tSelect Height Unit:")
                    height = ['Centimeters','Meters','Foot','Inches','Foot & Inches','Return to "Weight Unit" menu','Exit Program']
                    b = 0
                    while b < len(height):
                        print("\t {0}. {1}".format(b+1,height[b]))
                        b += 1
                    response2 = int(input("\tEnter choice number: "))
                    if response2 == 1:
                        cm = float(input("\tEnter  height in 'cm: "))
                        ht = cm
                    elif response2 == 2:
                        m = float(input("\tEnter height in 'm': "))
                        ht = m * 100
                    elif response2 == 3:
                        ft = float(input("\tEnter height in 'foot': "))
                        ht = ft * 30.48
                    elif response2 == 4:
                        inc = float(input("\tEnter height in 'inches': "))
                        ht = inc * 2.54
                    elif response2 == 5:
                        ft = float(input("\tEnter height in 'foot': ")) * 30.48
                        while True:    
                            inc = float(input("\tEnter height in 'inches': "))
                            if inc <= 12:
                                ht = ft + (inc * 2.54)
                            else:
                                print("\tInches must be between '0 to 12'.\n\t\tRe-enter!")
                                continue
                            break
                    elif response2 == 6:
                        bmi_calc()
                    elif response2 == 7:
                        exit()
                    elif response2 <= 0 or response2 > len(height):
                        print("\t*******************************\n\tIncorrect Choice! Select Again!")
                        continue
                    bmi = float(wt) / float(ht) / float(ht) * 100 * 100
                    print("""\n\t****************************""")
                    if bmi < 18.5 and bmi > 0:
                        print("\tOops!, You are Underweight")
                    elif bmi >= 18.5 and bmi <= 25:
                        print("\tCongrats! BMI is Normal")
                    elif bmi>25:
                        print("\tYou are Overweight, Take Care!")
                    print("\tYour BMI is : {0:.2f}\n\t****************************\n\t\t Thank You\n\t****************************\n".format(bmi))   
                    break
                break
        except Exception:
            print("\t********************************\n\tSomething went Wrong! Try Again!\n\t********************************\n")
            bmi_calc()
        finally:
            input("Press 'Enter' to calculate BMI ")

def exit():
    input("\nPress 'Enter' to calculate BMI ")
    bmi_calc()
    
bmi_calc()
