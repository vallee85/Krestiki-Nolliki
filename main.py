field = '''1 2 3
4 5 6
7 8 9'''
repit = 1


def win():
    global repit
    if field[:5:2] == "xxx": repit = -1; print("победа Крестикам!")
    if field[6:11:2] == "xxx": repit = -1; print("победа Крестикам!")
    if field[12:17:2] == "xxx": repit = -1; print("победа Крестикам!")
    if field[:13:6] == "xxx": repit = -1; print("победа Крестикам!")
    if field[2:15:6] == "xxx": repit = -1; print("победа Крестикам!")
    if field[4:17:6] == "xxx": repit = -1; print("победа Крестикам!")
    if field[:17:8] == "xxx": repit = -1; print("победа Крестикам!")
    if field[4:13:4] == "xxx": repit = -1; print("победа Крестикам!")
    if field[:5:2] == "ooo": repit = -1; print("победа Ноликам!")
    if field[6:11:2] == "ooo": repit = -1; print("победа Ноликам!")
    if field[12:17:2] == "ooo": repit = -1; print("победа Ноликам!")
    if field[:13:6] == "ooo": repit = -1; print("победа Ноликам!")
    if field[2:15:6] == "ooo": repit = -1; print("победа Ноликам!")
    if field[4:17:6] == "ooo": repit = -1; print("победа Ноликам!")
    if field[:17:8] == "ooo": repit = -1; print("победа Ноликам!")
    if field[4:13:4] == "ooo": repit = -1; print("победа Ноликам!")


print(field)
while repit > 0:
    x = field.replace(input('x введите номер вашего хода,'), str('x'))
    field = x
    print(field)
    win()
    o = field.replace(input('o введите номер вашего хода,'), str('o'))
    field = o
    print(field)
    win()
