# Body Mass Index Calculator
while True:
    try:
        print("""\t******Body Mass Index*******
\tSelect Weight Unit:""")
        weight = ['Kilograms','Ponds']
        a = 0
        while a < len(weight):
            print("\t {0}. {1}".format(a+1,weight[a]))
            a += 1
        response = int(input("\tEnter your choice: "))
        print()
        if response in range(len(weight)):
            if response == 1:
                kg = float(input("\tEnter your weight in kg: "))
                wt = kg
            elif response == 2:
                lbs = float(input("\tEnter your weight in lb: "))
                wt = lbs / 2.205  

            print("\n\tSelect Height Unit:")
            height = ['Centimeters','Meters','Foot','Inches','Foot & Inches']
            b = 0
            while b < len(height):
                print("\t {0}. {1}".format(b+1,height[b]))
                b += 1
            response = int(input("\tEnter your choice: "))
            print()
            if response == 1:
                cm = float(input("\tEnter your height in 'cm: "))
                ht = cm
            elif response == 2:
                m = float(input("\tEnter your height in 'm': "))
                ht = m * 100
            elif response == 3:
                ft = float(input("\tEnter your height in 'foot': "))
                ht = ft * 30.48
            elif response == 4:
                inc = float(input("\tEnter your height in 'inches': "))
                ht = inc * 2.54
            elif response == 5:
                ft = float(input("\tEnter your height in 'foot': ")) * 30.48
                inc = float(input("\tEnter your height in 'inches': ")) * 2.54
                ht = float(ft) + float(inc)
            else:
                print("""\t****************************
\tIncorrect Choice""")
                wt = 0
        else:
            print("""\t****************************
\tIncorrect Choice""")
            wt = 0
        if wt > 0:
            bmi = float(wt) / float(ht) / float(ht) * 100 * 100
            print("""\t****************************
\tYour BMI is : {0:.2f}""".format(bmi))
            
            if bmi < 18.5 and bmi > 0:
                print("\tOops!, You are Underweight")
            elif bmi >= 18.5 and bmi <= 25:
                print("\tCongrats! Your BMI is Normal")
            elif bmi>25:
                print("\tYou are Overweight, Take Care!")
            else:
                print("\tCan't Estimate")
            print("""\t****************************
\t\t Thank You
\t****************************""")
        else:
            print("\tCan't Estimated")
            print("""\t****************************
\t\t Try Again!
\t****************************""")    
    except Exception:
        print("""\t****************************
\t\t Try Again!
\t****************************""")
    finally:
        print(input("\nPress 'Enter' to calculate BMI "))