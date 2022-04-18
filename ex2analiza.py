import random


class Matrix:
    def _init_(self, row, coll):
        self.M = dict()
        self.Row = row
        self.Coll = coll
        for i in range(1, row + 1):
            for j in range(1, coll + 1):
                if i == j:
                    self.M[(i, j)] = 1
                else:
                    self.M[(i, j)] = 0

    def _str_(self):
        x = ''
        for i in range(1, self.Row + 1):
            x += str(list(self.M[(i, j)] for j in range(1, self.Coll + 1))) + '\n'
        return x

    def _add_(self, other):
        if self.Row != other.Row or self.Coll != other.Coll:
            return "Error"
        temp = Matrix(self.Row, self.Coll)
        for i in range(1, self.Row + 1):
            for j in range(1, other.Coll + 1):
                temp.M[(i, j)] = self.M[(i, j)] + other.M[(i, j)]
        return temp

    def _mul_(self, other):
        temp = Matrix(self.Row, other.Coll)
        for i in range(1, self.Row + 1):
            for j in range(1, other.Coll + 1):
                if i == j:
                    temp.M[(i, j)] = temp.M[(i, j)] - 1
                for k in range(1, other.Row + 1):
                    temp.M[(i, j)] += self.M[(i, k)] * other.M[(k, j)]

        return temp

    def getRow(self):
        return self.Row

    def getColl(self):
        return self.Coll

    def set_matrix(self):
        for i in range(1, self.Row + 1):
            for j in range(1, self.Coll + 1):
                self.M[(i, j)] = float(input(f'Please Enter M{[i, j]} :\n'))

    def Elementary_matrix(self, i, j, value):
        temp = Matrix(self.Row, self.Coll)
        temp.M[(i, j)] = value
        return temp

    def Line_replacement(self, x, y):
        temp1 = Matrix(self.Row, self.Coll)
        temp2 = Matrix(self.Row, self.Coll)
        for i in range(1, self.Coll + 1):
            temp1.M[(x, i)] = temp2.M[(y, i)]
            temp1.M[(y, i)] = temp2.M[(x, i)]
        print(print_mul(temp1, self))
        return temp1 * self


def Matrix_Rating(m):
    if m.Coll == m.Row + 1:
        temp = Matrix(m.Row, m.Coll - 1)
    else:
        temp = Matrix(m.Row, m.Coll)

    for i in range(1, m.Coll + 1):
        for j in range(i, m.Row + 1):
            if i == j:
                print(print_mul(temp.Elementary_matrix(j, i, 1 / m.M[(j, i)]), m))
                m = temp.Elementary_matrix(j, i, 1 / m.M[(j, i)]) * m
            else:
                print(print_mul(temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]), m))
                m = temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]) * m
    for i in list(range(1, m.Coll)._reversed_()):
        for j in list(range(1, i)._reversed_()):
            if i != j:
                print(print_mul(temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]), m))
                m = temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]) * m
    print("⏬  ⬇️final solution  ⬇️⏬")
    for i in range(1, m.Row + 1):
        print(f'  X[{i}] = {m.M[(i, m.Coll)]}')
    return m


def Pivot_order(m):
    for i in range(1, m.Coll + 1):
        for j in range(i, m.Row + 1):
            if abs(m.M[(j, i)]) > abs(m.M[(i, i)]):
                m = m.Line_replacement(i, j)
    return m


def print_mul(x, y):
    k = ''
    for i in range(1, x.Row + 1):
        if i == int(x.Row / 2 + 1):
            k += str(list(x.M[(i, j)] for j in range(1, x.Coll + 1))) + "  *  " + str(
                list(y.M[(i, j)] for j in range(1, y.Coll + 1))) + '  =  ' + str(
                list((x * y).M[(i, j)] for j in range(1, (x * y).Coll + 1)))
        else:
            k += str(list(x.M[(i, j)] for j in range(1, x.Coll + 1))) + "     " + str(
                list(y.M[(i, j)] for j in range(1, y.Coll + 1))) + "     " + str(
                list((x * y).M[(i, j)] for j in range(1, (x * y).Coll + 1)))
        k += '\n'

    return k


# def swap_matriX(M):


def swap_X_to_Slove(m):
    for i in range(1, m.Row + 1):
        m.M[(i, i)], m.M[(i, m.Coll)] = -1 * m.M[(i, m.Coll)], -1 * m.M[(i, i)]
    return m


def Jacoby(m):
    solution = {}
    for i in range(1, m.Row + 1):
        for j in range(i, m.Coll + 1):
            solution[(i)] = m.M[(i, m.Coll)]

    print("the arr sol", solution)
    for i in range(1, m.Row + 1):  # מחלק כל איבר בגודל של הPIVOT
        for j in range(1, m.Coll + 1):
            m.M[(i, j)] /= solution[i]

    print(m.M)
    print(solution)
    for i in range(1, m.Row + 1):  # מאפס SOLUTION את בחזרה ל1
        solution[i] /= solution[i]
    print(solution)


matrixA = [[12,2,0],[60,10,4],[0,31,5]]
vectorB=[[2],[6],[5]]

def check_max_Dominant(matrix):
    z = 1
    index_max = []
    for i in matrix:
        print("חיפוש האיבר המקסימלי בערך מוחלט בשורה: ")
        print(list(map(abs, i)))
        z = max(list(map(abs, i)))
        for j in range(len(i)):
            if z == abs(i[j]):
                if j in index_max:
                    return False
                index_max.append(j)
    print("אינדקסים של האיברים המקסימליים בכל שורה :")
    print(index_max)
    p = 0
    temp = []
    for i in matrix:
        temp.extend(i)
        print(f'print temp', temp)
        temp.remove(max(list(map(abs, temp))))
        if i[index_max[p]] <= sum(list(map(abs, temp))):
            return False
        p += 1
        temp.clear()
    return index_max


def NewOrderMatrix(information):
    if information:
        print("There's a dominant diagonal for the matrix.")
        p = 0
        newmatrix = []
        newvector = []
        for i in range(len(information)):
            newmatrix.append([])
            newvector.append(0)
        for i in information:
            newmatrix[i].extend(matrixA[p])
            newvector[i] = vectorB[p]
            p += 1
        return newmatrix,newvector
    else:
        print("There is no dominant diagonal in the matrix.")
        for i in range(len(matrixA)):
            for j in range(i, len(matrixA)):
                if abs(matrixA[j][i]) > abs(matrixA[i][i]):
                    print("Pivot_order<---", matrixA, vectorB)
                    matrixA[i],matrixA[j] = matrixA[j], matrixA[i]
                    vectorB[i], vectorB[j] = vectorB[j], vectorB[i]
                    print("Pivot_order--->", matrixA, vectorB)
        return matrixA,vectorB


matrixA,vectorB=NewOrderMatrix(check_max_Dominant(matrixA))




"""
m = Matrix(2,3)
m.set_matrix()

t= swap_X_to_Slove(m)
print(f'the solution arr is\n{t} \n')
Jacoby(t)"""
"""
m1 = Matrix(3,4)
m1.set_matrix()
m1 = Matrix_Rating(Pivot_order(m1))
print(f'\n*Final and correct matrix*\n{m1}')
"""
