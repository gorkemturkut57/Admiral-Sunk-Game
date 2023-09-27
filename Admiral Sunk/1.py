def find_the_value(x):
    if str(x) == "A":
        VALUE = 0
    elif str(x) == "B":
        VALUE = 1
    elif str(x) == "C":
        VALUE = 2
    elif str(x) == "D":
        VALUE = 3
    elif str(x) == "E":
        VALUE = 4
    elif str(x) == "F":
        VALUE = 5
    elif str(x) == "G":
        VALUE = 6
    else:
        VALUE = 7
    return int(VALUE)
def find_the_letter(x): #Indexleri uygun harflere dönüştüren fonksiyon.
    if x == 0:
        LETTER = "A"
    elif x == 1:
        LETTER = "B"
    elif x == 2:
        LETTER = "C"
    elif x == 3:
        LETTER = "D"
    elif x == 4:
        LETTER = "E"
    elif x == 5:
        LETTER = "F"
    elif x == 6:
        LETTER = "G"
    elif x == 7:
        LETTER = "H"
    return LETTER
def get_the_number_of_lines():
    go="y"
    while go=="y":
        try:
            number_of_lines = int(input("Enter the number of lines(5-7)"))
            if 5<= number_of_lines <= 7:
                go = "n"
            else:
                print("Please enter a value which is between 5-7!")
        except:
            print("Please enter a valid value!")
    return number_of_lines
LINES=get_the_number_of_lines()
COLUMNS=LINES+1
def print_the_chart(number_of_lines):
    all_letters=["A","B","C","D","E","F","G","H"]
    available_letters=[]
    count=0
    for letter in all_letters:
        count+=1
        available_letters.append(letter)
        if count==COLUMNS:
            break
    play_list=[]
    for i in range(1,number_of_lines+1):
        columns=[]
        for j in range(1,number_of_lines+2):
            columns.append("*")
            if j==COLUMNS:
                play_list.append(columns)
    line_no=0
    for i in available_letters:
        if available_letters.index(i)!=COLUMNS-1:
            print(i, end="   ")
        else:
            print(i)
    for i in play_list:
        line_no+=1
        column_no=0
        if line_no!=1 and line_no!=LINES+1:
            print("|   "*COLUMNS)
        for j in i:
            column_no+=1
            if column_no==COLUMNS:
                print(j,line_no)
            else:
                print(j,end="---")
    return play_list,available_letters
game_list,available_letters=print_the_chart(LINES)
white_list=game_list
black_list=game_list
def print_the_continuation_of_the_chart(list):
    line_no = 0
    for i in available_letters:
        if available_letters.index(i) != COLUMNS - 1:
            print(i, end="   ")
        else:
            print(i)
    for i in list:
        line_no += 1
        column_no = 0
        if line_no != 1 and line_no != LINES + 1:
            print("|   " * COLUMNS)
        for j in i:
            column_no += 1
            if column_no == COLUMNS:
                print(j, line_no)
            else:
                print(j, end="---")
def put_the_white_ships():
    white_ships_coordinations=[]
    print("There are one 2x,one 3x,one 4x and one 5x white ships,position them wisely!")
    go = "y"
    while go == "y":
        try:
            put_the_5x_ship=input("Enter the first and last coordinates of the 5x ship:")
            put_the_5x_ship=put_the_5x_ship.upper()
            LINE_INDEX1=int(put_the_5x_ship[1])-1
            COLUMN_INDEX1=find_the_value(put_the_5x_ship[0])
            LINE_INDEX2 = int(put_the_5x_ship[4])- 1
            COLUMN_INDEX2 = find_the_value(put_the_5x_ship[3])
            if len(put_the_5x_ship)==5 and put_the_5x_ship[0] in available_letters and put_the_5x_ship[3] in available_letters and int(put_the_5x_ship[1])<=COLUMNS and int(put_the_5x_ship[4])<=COLUMNS:
                if put_the_5x_ship[0]==put_the_5x_ship[3] and abs(int(put_the_5x_ship[1])-int(put_the_5x_ship[4]))==4:
                    go="n"
                    if LINE_INDEX1<LINE_INDEX2:
                        for i in range(LINE_INDEX1, LINE_INDEX1 + 5):
                            white_list[i][COLUMN_INDEX1] = "W"
                            white_ships_coordinations.append(put_the_5x_ship[0] + str(i + 1))
                    else:
                        for i in range(LINE_INDEX2, LINE_INDEX2 + 5):
                            white_list[i][COLUMN_INDEX1] = "W"
                            white_ships_coordinations.append(put_the_5x_ship[0] + str(i + 1))
                elif put_the_5x_ship[1]==put_the_5x_ship[4] and abs(COLUMN_INDEX1-COLUMN_INDEX2)==4:
                    go="n"
                    if COLUMN_INDEX1<COLUMN_INDEX2:
                        for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 5):
                            white_list[LINE_INDEX1][i] = "W"
                            white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                    else:
                        for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 5):
                            white_list[LINE_INDEX1][i] = "W"
                            white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                else:
                    print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(white_list)
    go = "y"
    while go == "y":
        try:
            put_the_4x_ship = input("Enter the first and last coordinates of the 4x ship:")
            put_the_4x_ship = put_the_4x_ship.upper()
            LINE_INDEX1 = int(put_the_4x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_4x_ship[0])
            LINE_INDEX2 = int(put_the_4x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_4x_ship[3])
            if len(put_the_4x_ship) == 5 and put_the_4x_ship[0] in available_letters and put_the_4x_ship[3] in available_letters and int(put_the_4x_ship[1]) <= COLUMNS and int(put_the_4x_ship[4]) <= COLUMNS:
                coordinations=[]
                if put_the_4x_ship[0] == put_the_4x_ship[3] and abs(int(put_the_4x_ship[1]) - int(put_the_4x_ship[4])) == 3:
                    if int(put_the_4x_ship[1])<int(put_the_4x_ship[4]):
                        for i in range(int(put_the_4x_ship[1]), int(put_the_4x_ship[1]) + 4):
                            coordinations.append(put_the_4x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_4x_ship[4]), int(put_the_4x_ship[1]) + 4):
                            coordinations.append(put_the_4x_ship[0] + str(i))
                    done=0
                    for j in coordinations:
                        if j in white_ships_coordinations:
                            done=1
                            break
                    if done==0:
                        go = "n"
                        if LINE_INDEX1<LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 4):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_4x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 4):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_4x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_4x_ship[1] == put_the_4x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 3:
                   if COLUMN_INDEX1<COLUMN_INDEX2:
                       for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 4):
                           coordinations.append(find_the_letter(i) + str(put_the_4x_ship[4]))
                   else:
                       for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 4):
                           coordinations.append(find_the_letter(i) + str(put_the_4x_ship[4]))
                   done = 0
                   for j in coordinations:
                       if j in white_ships_coordinations:
                           done = 1
                           break
                   if done == 0:
                       go = "n"
                       if COLUMN_INDEX1 < COLUMN_INDEX2:
                           for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 4):
                               white_list[LINE_INDEX1][i] = "W"
                               white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                       else:
                           for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 4):
                               white_list[LINE_INDEX1][i] = "W"
                               white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                   else:
                       print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(white_list)
    go = "y"
    while go == "y":
        try:
            put_the_3x_ship = input("Enter the first and last coordinates of the 3x ship:")
            put_the_3x_ship = put_the_3x_ship.upper()
            LINE_INDEX1 = int(put_the_3x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_3x_ship[0])
            LINE_INDEX2 = int(put_the_3x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_3x_ship[3])
            if len(put_the_3x_ship) == 5 and put_the_3x_ship[0] in available_letters and put_the_3x_ship[3] in available_letters and int(put_the_3x_ship[1]) <= COLUMNS and int(put_the_3x_ship[4]) <= COLUMNS:
                coordinations=[]
                if put_the_3x_ship[0] == put_the_3x_ship[3] and abs(int(put_the_3x_ship[1]) - int(put_the_3x_ship[4])) == 2:
                    if int(put_the_3x_ship[1])<int(put_the_3x_ship[4]):
                        for i in range(int(put_the_3x_ship[1]), int(put_the_3x_ship[1]) + 3):
                            coordinations.append(put_the_3x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_3x_ship[4]), int(put_the_3x_ship[1]) + 3):
                            coordinations.append(put_the_3x_ship[0] + str(i))
                    done=0
                    for j in coordinations:
                        if j in white_ships_coordinations:
                            done=1
                            break
                    if done==0:
                        go = "n"
                        if LINE_INDEX1<LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 3):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_3x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 3):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_3x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_3x_ship[1] == put_the_3x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 2:
                   if COLUMN_INDEX1<COLUMN_INDEX2:
                       for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 3):
                           coordinations.append(find_the_letter(i) + str(put_the_3x_ship[4]))
                   else:
                       for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 3):
                           coordinations.append(find_the_letter(i) + str(put_the_3x_ship[4]))
                   done = 0
                   for j in coordinations:
                       if j in white_ships_coordinations:
                           done = 1
                           break
                   if done == 0:
                       go = "n"
                       if COLUMN_INDEX1 < COLUMN_INDEX2:
                           for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 3):
                               white_list[LINE_INDEX1][i] = "W"
                               white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                       else:
                           for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 3):
                               white_list[LINE_INDEX1][i] = "W"
                               white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                   else:
                       print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(white_list)
    go = "y"
    while go == "y":
        try:
            put_the_2x_ship = input("Enter the first and last coordinates of the 2x ship:")
            put_the_2x_ship = put_the_2x_ship.upper()
            LINE_INDEX1 = int(put_the_2x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_2x_ship[0])
            LINE_INDEX2 = int(put_the_2x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_2x_ship[3])
            if len(put_the_2x_ship) == 5 and put_the_2x_ship[0] in available_letters and put_the_2x_ship[
                3] in available_letters and int(put_the_2x_ship[1]) <= COLUMNS and int(put_the_2x_ship[4]) <= COLUMNS:
                coordinations = []
                if put_the_2x_ship[0] == put_the_2x_ship[3] and abs(
                        int(put_the_2x_ship[1]) - int(put_the_2x_ship[4])) == 1:
                    if int(put_the_2x_ship[1]) < int(put_the_2x_ship[4]):
                        for i in range(int(put_the_2x_ship[1]), int(put_the_2x_ship[1]) + 2):
                            coordinations.append(put_the_2x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_2x_ship[4]), int(put_the_2x_ship[1]) + 2):
                            coordinations.append(put_the_2x_ship[0] + str(i))
                    done = 0
                    for j in coordinations:
                        if j in white_ships_coordinations:
                            done = 1
                            break
                    if done == 0:
                        go = "n"
                        if LINE_INDEX1 < LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 2):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_2x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 2):
                                white_list[i][COLUMN_INDEX1] = "W"
                                white_ships_coordinations.append(put_the_2x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_2x_ship[1] == put_the_2x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 1:
                    if COLUMN_INDEX1 < COLUMN_INDEX2:
                        for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 2):
                            coordinations.append(find_the_letter(i) + str(put_the_2x_ship[4]))
                    else:
                        for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 2):
                            coordinations.append(find_the_letter(i) + str(put_the_2x_ship[4]))
                    done = 0
                    for j in coordinations:
                        if j in white_ships_coordinations:
                            done = 1
                            break
                    if done == 0:
                        go = "n"
                        if COLUMN_INDEX1 < COLUMN_INDEX2:
                            for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 2):
                                white_list[LINE_INDEX1][i] = "W"
                                white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                        else:
                            for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 2):
                                white_list[LINE_INDEX1][i] = "W"
                                white_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                    else:
                        print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(white_list)
    return white_ships_coordinations
WHITE_COORDINATIONS=put_the_white_ships()
def create_the_list():
    all_letters=["A","B","C","D","E","F","G","H"]
    available_letters=[]
    count=0
    for letter in all_letters:
        count+=1
        available_letters.append(letter)
        if count==COLUMNS:
            break
    LIST=[]
    for i in range(1,LINES+1):
        columns=[]
        for j in range(1,LINES+2):
            columns.append("*")
            if j==COLUMNS:
                LIST.append(columns)
    return LIST
def put_the_black_ships():
    black_list=create_the_list()
    black_ships_coordinations=[]
    print_the_continuation_of_the_chart(black_list)
    print("There are one 2x,one 3x,one 4x and one 5x black ships,position them wisely!")
    go = "y"
    while go == "y":
        try:
            put_the_5x_ship=input("Enter the first and last coordinates of the 5x ship:")
            put_the_5x_ship=put_the_5x_ship.upper()
            LINE_INDEX1=int(put_the_5x_ship[1])-1
            COLUMN_INDEX1=find_the_value(put_the_5x_ship[0])
            LINE_INDEX2 = int(put_the_5x_ship[4])- 1
            COLUMN_INDEX2 = find_the_value(put_the_5x_ship[3])
            if len(put_the_5x_ship)==5 and put_the_5x_ship[0] in available_letters and put_the_5x_ship[3] in available_letters and int(put_the_5x_ship[1])<=COLUMNS and int(put_the_5x_ship[4])<=COLUMNS:
                if put_the_5x_ship[0]==put_the_5x_ship[3] and abs(int(put_the_5x_ship[1])-int(put_the_5x_ship[4]))==4:
                    go="n"
                    if LINE_INDEX1<LINE_INDEX2:
                        for i in range(LINE_INDEX1, LINE_INDEX1 + 5):
                            black_list[i][COLUMN_INDEX1] = "B"
                            black_ships_coordinations.append(put_the_5x_ship[0] + str(i + 1))
                    else:
                        for i in range(LINE_INDEX2, LINE_INDEX2 + 5):
                            black_list[i][COLUMN_INDEX1] = "B"
                            black_ships_coordinations.append(put_the_5x_ship[0] + str(i + 1))
                elif put_the_5x_ship[1]==put_the_5x_ship[4] and abs(COLUMN_INDEX1-COLUMN_INDEX2)==4:
                    go="n"
                    if COLUMN_INDEX1<COLUMN_INDEX2:
                        for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 5):
                            black_list[LINE_INDEX1][i] = "B"
                            black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                    else:
                        for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 5):
                            black_list[LINE_INDEX1][i] = "B"
                            black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                else:
                    print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(black_list)
    go = "y"
    while go == "y":
        try:
            put_the_4x_ship = input("Enter the first and last coordinates of the 4x ship:")
            put_the_4x_ship = put_the_4x_ship.upper()
            LINE_INDEX1 = int(put_the_4x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_4x_ship[0])
            LINE_INDEX2 = int(put_the_4x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_4x_ship[3])
            if len(put_the_4x_ship) == 5 and put_the_4x_ship[0] in available_letters and put_the_4x_ship[3] in available_letters and int(put_the_4x_ship[1]) <= COLUMNS and int(put_the_4x_ship[4]) <= COLUMNS:
                coordinations=[]
                if put_the_4x_ship[0] == put_the_4x_ship[3] and abs(int(put_the_4x_ship[1]) - int(put_the_4x_ship[4])) == 3:
                    if int(put_the_4x_ship[1])<int(put_the_4x_ship[4]):
                        for i in range(int(put_the_4x_ship[1]), int(put_the_4x_ship[1]) + 4):
                            coordinations.append(put_the_4x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_4x_ship[4]), int(put_the_4x_ship[1]) + 4):
                            coordinations.append(put_the_4x_ship[0] + str(i))
                    done=0
                    for j in coordinations:
                        if j in black_ships_coordinations:
                            done=1
                            break
                    if done==0:
                        go = "n"
                        if LINE_INDEX1<LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 4):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_4x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 4):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_4x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_4x_ship[1] == put_the_4x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 3:
                   if COLUMN_INDEX1<COLUMN_INDEX2:
                       for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 4):
                           coordinations.append(find_the_letter(i) + str(put_the_4x_ship[4]))
                   else:
                       for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 4):
                           coordinations.append(find_the_letter(i) + str(put_the_4x_ship[4]))
                   done = 0
                   for j in coordinations:
                       if j in black_ships_coordinations:
                           done = 1
                           break
                   if done == 0:
                       go = "n"
                       if COLUMN_INDEX1 < COLUMN_INDEX2:
                           for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 4):
                               black_list[LINE_INDEX1][i] = "B"
                               black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                       else:
                           for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 4):
                               black_list[LINE_INDEX1][i] = "B"
                               black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                   else:
                       print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(black_list)
    go = "y"
    while go == "y":
        try:
            put_the_3x_ship = input("Enter the first and last coordinates of the 3x ship:")
            put_the_3x_ship = put_the_3x_ship.upper()
            LINE_INDEX1 = int(put_the_3x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_3x_ship[0])
            LINE_INDEX2 = int(put_the_3x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_3x_ship[3])
            if len(put_the_3x_ship) == 5 and put_the_3x_ship[0] in available_letters and put_the_3x_ship[3] in available_letters and int(put_the_3x_ship[1]) <= COLUMNS and int(put_the_3x_ship[4]) <= COLUMNS:
                coordinations=[]
                if put_the_3x_ship[0] == put_the_3x_ship[3] and abs(int(put_the_3x_ship[1]) - int(put_the_3x_ship[4])) == 2:
                    if int(put_the_3x_ship[1])<int(put_the_3x_ship[4]):
                        for i in range(int(put_the_3x_ship[1]), int(put_the_3x_ship[1]) + 3):
                            coordinations.append(put_the_3x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_3x_ship[4]), int(put_the_3x_ship[1]) + 3):
                            coordinations.append(put_the_3x_ship[0] + str(i))
                    done=0
                    for j in coordinations:
                        if j in black_ships_coordinations:
                            done=1
                            break
                    if done==0:
                        go = "n"
                        if LINE_INDEX1<LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 3):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_3x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 3):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_3x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_3x_ship[1] == put_the_3x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 2:
                   if COLUMN_INDEX1<COLUMN_INDEX2:
                       for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 3):
                           coordinations.append(find_the_letter(i) + str(put_the_3x_ship[4]))
                   else:
                       for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 3):
                           coordinations.append(find_the_letter(i) + str(put_the_3x_ship[4]))
                   done = 0
                   for j in coordinations:
                       if j in black_ships_coordinations:
                           done = 1
                           break
                   if done == 0:
                       go = "n"
                       if COLUMN_INDEX1 < COLUMN_INDEX2:
                           for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 3):
                               black_list[LINE_INDEX1][i] = "B"
                               black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                       else:
                           for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 3):
                               black_list[LINE_INDEX1][i] = "B"
                               black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                   else:
                       print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(black_list)
    go = "y"
    while go == "y":
        try:
            put_the_2x_ship = input("Enter the first and last coordinates of the 2x ship:")
            put_the_2x_ship = put_the_2x_ship.upper()
            LINE_INDEX1 = int(put_the_2x_ship[1]) - 1
            COLUMN_INDEX1 = find_the_value(put_the_2x_ship[0])
            LINE_INDEX2 = int(put_the_2x_ship[4]) - 1
            COLUMN_INDEX2 = find_the_value(put_the_2x_ship[3])
            if len(put_the_2x_ship) == 5 and put_the_2x_ship[0] in available_letters and put_the_2x_ship[
                3] in available_letters and int(put_the_2x_ship[1]) <= COLUMNS and int(put_the_2x_ship[4]) <= COLUMNS:
                coordinations = []
                if put_the_2x_ship[0] == put_the_2x_ship[3] and abs(
                        int(put_the_2x_ship[1]) - int(put_the_2x_ship[4])) == 1:
                    if int(put_the_2x_ship[1]) < int(put_the_2x_ship[4]):
                        for i in range(int(put_the_2x_ship[1]), int(put_the_2x_ship[1]) + 2):
                            coordinations.append(put_the_2x_ship[0] + str(i))
                    else:
                        for i in range(int(put_the_2x_ship[4]), int(put_the_2x_ship[1]) + 2):
                            coordinations.append(put_the_2x_ship[0] + str(i))
                    done = 0
                    for j in coordinations:
                        if j in black_ships_coordinations:
                            done = 1
                            break
                    if done == 0:
                        go = "n"
                        if LINE_INDEX1 < LINE_INDEX2:
                            for i in range(LINE_INDEX1, LINE_INDEX1 + 2):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_2x_ship[0] + str(i + 1))
                        else:
                            for i in range(LINE_INDEX2, LINE_INDEX2 + 2):
                                black_list[i][COLUMN_INDEX1] = "B"
                                black_ships_coordinations.append(put_the_2x_ship[0] + str(i + 1))
                    else:
                        print("Please enter a valid value!")
                elif put_the_2x_ship[1] == put_the_2x_ship[4] and abs(COLUMN_INDEX1 - COLUMN_INDEX2) == 1:
                    if COLUMN_INDEX1 < COLUMN_INDEX2:
                        for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 2):
                            coordinations.append(find_the_letter(i) + str(put_the_2x_ship[4]))
                    else:
                        for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 2):
                            coordinations.append(find_the_letter(i) + str(put_the_2x_ship[4]))
                    done = 0
                    for j in coordinations:
                        if j in black_ships_coordinations:
                            done = 1
                            break
                    if done == 0:
                        go = "n"
                        if COLUMN_INDEX1 < COLUMN_INDEX2:
                            for i in range(COLUMN_INDEX1, COLUMN_INDEX1 + 2):
                                black_list[LINE_INDEX1][i] = "B"
                                black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                        else:
                            for i in range(COLUMN_INDEX2, COLUMN_INDEX2 + 2):
                                black_list[LINE_INDEX1][i] = "B"
                                black_ships_coordinations.append(find_the_letter(i) + str(LINE_INDEX1 + 1))
                    else:
                        print("Please enter a valid value!")
                else:
                    print("Please enter a valid value!")
            else:
                print("Please enter a valid value!")
        except:
            print("Please enter a valid value!")
    print_the_continuation_of_the_chart(black_list)
    return black_list,black_ships_coordinations
BLACK_LIST,BLACK_COORDINATIONS=put_the_black_ships()
GAME_LIST1 = create_the_list()
def white_strike(black_list):

    go="y"
    while go=="y":
        stike_coordinations=input("Enter the coordinations of strikes:")
        stike_coordinations=stike_coordinations.upper()
        if len(stike_coordinations)==2 and stike_coordinations[0] in available_letters and int(stike_coordinations[1])<=COLUMNS:
            LINE_INDEX = int(stike_coordinations[1]) - 1
            COLUMN_INDEX = find_the_value(stike_coordinations[0])
            go="n"
            if stike_coordinations in black_list:
                GAME_LIST1[LINE_INDEX][COLUMN_INDEX]="S"
            else:
                GAME_LIST1[LINE_INDEX][COLUMN_INDEX] = "M"
            print_the_continuation_of_the_chart(GAME_LIST1)
        else:
            print("Please enter a valid value!")
GAME_LIST2 = create_the_list()
def black_strike(white_coordinations):
    go = "y"
    while go == "y":
        stike_coordinations = input("Enter the coordinations of strikes:")
        stike_coordinations = stike_coordinations.upper()
        if len(stike_coordinations) == 2 and stike_coordinations[0] in available_letters and int(
                stike_coordinations[1]) <= COLUMNS:
            LINE_INDEX = int(stike_coordinations[1]) - 1
            COLUMN_INDEX = find_the_value(stike_coordinations[0])
            go = "n"
            if stike_coordinations in white_coordinations:
                GAME_LIST2[LINE_INDEX][COLUMN_INDEX] = "S"
            else:
                GAME_LIST2[LINE_INDEX][COLUMN_INDEX] = "M"
            print_the_continuation_of_the_chart(GAME_LIST2)
        else:
            print("Please enter a valid value!")
def main():
    try:
        order_of_movement = -1
        while True:
            order_of_movement += 1
            if order_of_movement % 2 == 0:
                white_strike(BLACK_COORDINATIONS)
            else:
                black_strike(WHITE_COORDINATIONS)
            white_shoots=[]
            black_shoots=[]
            for i in GAME_LIST1:
                for j in i:
                    white_shoots.append(j)
            for i in GAME_LIST2:
                for j in i:
                    black_shoots.append(j)
            if white_shoots.count("S")==14:
                print("White player is the winner!")
                break
            elif black_shoots.count("S")==14:
                print("Black player is the winner!")
                break
    except:
        print("Please enter a valid value!")

main()
