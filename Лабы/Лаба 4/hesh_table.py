class Hesh_Table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.capacity = 0

    def __retable(self):#Вставляем в новую таблицу значения из старой, перехешируя их
        new_size = self.size*2
        new_table = [[] for _ in range(new_size)]

        old_table = self.table

        self.table = new_table
        self.size = new_size
        self.capacity = 0

        for i in old_table:
            if len(i) != 0:
                if i[0] != None:
                    self.insert(i[0],i[1])

    def __probing(self, i, key, val):#Функция разрешающая колизии
        i = i + 1
        while True:
            # Если уперлись в конец списка, начинаем с начала
            if i >= self.size:
                i = 0
            #Новое значение
            if len(self.table[i]) == 0:
                self.table[i] = [key, val]
                self.capacity += 1
                break
            #Замена значения
            elif self.table[i][0] == key:
                self.table[i][1] = val
                break

            else:
                i += 1


    def insert(self, key, val):
        index = hash(key) % self.size
        if (len(self.table[index])==0) or self.table[index][0] == None:
            self.table[index] = [key,val]
            self.capacity += 1

        elif self.table[index][0] == key:
            self.table[index][1] = val

        else:
            self.__probing(index, key, val)
        #Если заполненость больше 70%: увеличиваем размер в два раза
        if self.capacity / self.size >= 0.7:
            self.__retable()

    def get(self,key):
        index = hash(key) % self.size

        if len(self.table[index]) != 0 and self.table[index][0] == key:
            return self.table[index][1]

        i = index + 1
        iter = 0

        while iter < self.size:
            iter+=1
            if i >= self.size:
                i = 0
            if len(self.table[index]) != 0 and self.table[index][0] == key:
                return self.table[index][1]
            i+=1
        return False

    def delete(self, key):
        index = hash(key) % self.size

        if len(self.table[index]) != 0 and self.table[index][0] == key:
            self.table[index][0] = None
            return True

        i = index + 1
        iter = 0

        while iter < self.size:
            iter += 1
            if i >= self.size:
                i = 0
            if len(self.table[index]) != 0 and self.table[index][0] == key:
                self.table[index][0] = None
                return True
            i += 1
        return False





ht = Hesh_Table(5)
ht.insert(0,'привет')
ht.insert(1,'привет')
ht.insert(2,'привет')
print(ht.get(4))

print(ht.delete(2))
print(ht.get(2))

