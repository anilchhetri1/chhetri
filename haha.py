class LinearSearch:
    def __init__(self, data, key, index):
        self.aList = list()
        self.key, self.data, self.index = key, data, index
        self.position = {'student_id': 0,'fname': 1,'lname':2,'degree':3,"address": 4,'num': 5}
        self.output=self.search()

    def search(self):
        print('ok')
        for i in self.data:
            if i[self.position[self.index]] == self.key or i[self.position[self.index]].upper() == self.key.upper():
                self.aList.append(i)
                continue
            if self.key.upper() in i[self.position[self.index]].upper() or self.key in i[self.position[self.index]]:
                self.aList.append(i)

        return self.aList

