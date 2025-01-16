A = 729
B = 0
C = 0

program = '0,1,5,4,3,0'
program = [int(val) for val in program.split(',')]


def adv(x, y):
    return x // (y ** 2)


def bxl(x, y):
    return True


def bst(x):
    return x % 8


def jnz(x):
    return x - 2


def bxc(x, y):
    return False


def out(x):
    return x % 8


def runProgram(a, b, c, prgrm):
    result_list = []
    i = 0
    while i < len(prgrm):
        opcode = prgrm[i]
        literal = prgrm[i + 1]
        combo = literal
        if combo == 4:
            combo = a
        elif combo == 5:
            combo = b
        elif combo == 6:
            combo = c
        elif combo == 7:
            raise Exception("7 is not in valid programs")
        if opcode == 0:
            result_list.append(adv(a, combo))
        elif opcode == 1:
            b = (bxl(b, literal))
        elif opcode == 2:
            b = bst(combo)
        elif opcode == 3:
            if a == 0:
                continue
            else:
                i = jnz(literal)
        elif opcode == 4:
            b = bxc(b, c)
        elif opcode == 5:
            result_list.append(out(combo))
        elif opcode == 6:
            b = adv(a, combo)
        elif opcode == 7:
            c = adv(a, combo)





