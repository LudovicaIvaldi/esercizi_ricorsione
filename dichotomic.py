def dichotomic(input_list, val):
    if len(input_list) == 1:
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        index = len(input_list)//2
        #basterebbe cercare solo in una delle 2 perchè se val è maggiore conviene gardare solo sopr
        #se val è monire conviene guardare oslo la sotto
        element=input_list[index]
        if element == val:
            return True
        elif val < element:
            return dichotomic(input_list[:index], val)
        elif val > element:
            return dichotomic(input_list[index:], val)



if __name__ == "__main__":
    lista=[1,2,3,4,5,6,7,8,9,10]
    print(dichotomic(lista, 5))
    print(dichotomic(lista, 12))