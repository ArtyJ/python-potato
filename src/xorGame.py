from random import randint

def inputIntLessThan(current, options):
    while True:
        data = input(f"Input a smaller number to replace {current} without duplicating the other two: ")
        try:
            inputData = eval(data)
            if type(inputData) == int:
                if inputData > 0 and inputData < current and inputData not in options:
                    # print(f"challenger input {inputData}")
                    return inputData
        except:
            pass


def challengerTurn(options):
    print()
    print()
    print('now it is your turn.')
    while True:
        data = input(f"Choose a number to reduce within {options[0]}, {options[1]}, and {options[2]}: ")
        try:
            inputData = eval(data)
            if type(inputData) == int:
                if inputData in options:
                    newNum = inputIntLessThan(inputData, options)
                    print(f"challenger reduced {inputData} to {newNum}")
                    return newNum
        except:
            pass
        
    
"""
        no = input('please enter a new smaller positive integer.')
"""
if __name__ == '__main__': 
    
    # description of game rules
    print("")
    print("")
    print("the game starts with randomly generating three different integers. one of the two players, staring from you, should")
    print("in turns choose only one from the three numbers and replace it with a new smaller positive integer, which is to be ")
    print("different from other two unchanged numbers. if any side fails to do so, the other one is winner. the game is over. ")

    # randomly generate three different integers
    from random import randint
    no1 = randint(15,125)
    no2 = randint(15,125)
    while no2 == no1:
        no2 = randint(15,125)
    no3 = randint(15,125)
    while no3 == no1 or no3 == no2:
        no3 = randint(15,125)
    options = sorted([no1, no2, no3])
    print("")
    print(f"first no. {options[0]}     second no. {options[1]}     third no. {options[2]}")
    
    challengerTurn(options)

# numb1 = prepare(40,60)
# numb2 = prepare(50,80)
# numb3 = prepare(17,43)

# numb = []
# for i in range(0,7): 
#     nob = numb1[i]+numb2[i]+numb3[i]
#     # print(numb1[i]+numb2[i]+numb3[i])
#     numb.append(nob)
# print(numb)

# for i in range(0,7):
#     if numb[i] % 2 == 0 and i !=6: continue
#     if numb[i] == 1:
#         if numb1[i] == 1:
#             j = 1
#             my_step()
#         elif numb2[i] == 1:
#             j = 2
#             my_step()
#         else:
#             j = 3
#             my_step()
#     j = randint(1,3) # numb[i] == 3
#     my_step()
#     # perfect conbination
