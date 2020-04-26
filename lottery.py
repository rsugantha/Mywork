import random

def menu():
    user_num = get_player_number()
    lot_num = create_lottery_num()

    matched_num= user_num.intersection(lot_num)
    print("You matched {}. You won ${}".format (matched_num, 100**len(matched_num)))

          
def get_player_number():
    num_csv=input("enter numbers with comma")
    num_list=num_csv.split(',')
    int_set ={int(num) for num in num_list}
    return int_set

def create_lottery_num():

    values= set()
    while(len(values)<6):
          values.add(random.randint(1,20))
    return values



menu()

          
