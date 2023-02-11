user = {'pin':1804,
        'balance':500000,
        'limited_balance':50000,
        }

      

def withdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you want to widthdraw: "))
        if amount > user['balance']:
            print("you have insufficent balance in your account \n please check your balance try agaian")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} rupess successfully debit to your account \n your remaining balance is  { user['balance']} rupess")
            print('')
            return False


def balance_enquiry():
  print(f"Total balance { user['balance']} rupees")
  print('')

def deposit():
   while True:
        amount = int(input("Enter the amount of money you want to deposit: "))
        if amount > user['limited_balance']:
            print("overloaded")
        else:
            user['balance'] = user['balance'] + amount
            print(f"{amount} rupess successfully credit to your account \n your present balance is  { user['balance']} rupess")
            print('')
            return False



def pin_generation(old_pin,new_pin):
  global user_pin

  if not old_pin == userpin:
    print('Invalid old PIN, Please try again or visit the nearest branch')
  else:
    userpin = new_pin
    print('ATM Card PIN ending with xx23 is updated Successfully!')
is_quit = False
print('')
print("Welcome to the Peoples Bank of india ATM serives")

pin = int(input('Please enter your four digit pin: '))

if pin == user['pin']:
    while is_quit == False:
        print("what do you want to do\n")
        print("1.withdraw_cash",12*" ",'2.Balance_enquiry\n')
        print('3.deposit',19*" ",'4.Pin Generation\n')
        print('5.exit\n')

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            withdraw_cash()
        elif query == 2:
            balance_enquiry()
        elif query == 3:
            deposit()
        elif query == 4:
          old_pin = int(input("Enter Your Current PIN: "))
          new_pin = int(input('Enter New PIN: '))
          pin_generation(old_pin,new_pin)
        elif query == 5:
          is_quit=True

          
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong pin")

