'''
     CS5001
     Spring 2022
     HW1
 
     Chenxuan Xu
'''

def main():

    # get the fee and kWh used from user (input)
    supplier_fee = float(input("What is the supplier fee per kWh?: "))
    power_fee = float(input("What is the power fee per kWh?: "))
    kWh_used = float(input("How many kWh were used this month?: "))
    
    # compute the charge and bill
    supply_charge = supplier_fee * kWh_used
    power_delivery_charge = power_fee * kWh_used
    total = supply_charge + power_delivery_charge

    # output final bill to user
    print(f" Your electric bill this month is ${total:.2f}")


if __name__ == "__main__":
    main()
    
