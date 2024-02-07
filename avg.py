class Test:
    def __init__(self):
        self.fds = []
        self.n = 0


    def getdata(self):
        self.n = int(input('\nEnter the class strength of SE Comp A: '))
        print('\n(Note: Enter -1 for absent students)\n')
        print('Enter the marks scored in Fundamental of Data Structure: ')
        for i in range(self.n):
            self.fds.append(int(input(f'Enter marks of roll no {i + 1}: ')))


    def putdata(self):
        print('\n\nTest Marks of Fundamental of Data Structure are as follows...\n')
        print('|    Roll No    |   DSA Marks   |')
        

        for i in range(self.n):
            print(f'|\t{i + 1}\t|\t{self.fds[i]}\t|')
       

    def avg(self):
        total = 0
        present = 0
        for i in self.fds:
            if i != -1:
                total += i
                present += 1

        print(f'Average marks of the class: {round(total / present, 3)}\n\n')


    def absstud(self):
        print('Students absent for Fundamental of Data Structure test are: \n')
        absent = 0
        for i in range(self.n):
            if self.fds[i] == -1:
                print(f'Roll No: {i + 1} absent')
                absent += 1

        print(f'\nTotal absent students are: {absent}\n\n')


    def maxmin(self):
        maxi, max_rollno, mini, min_rollno = 0, [], 10, []
        for i, val in enumerate(self.fds):
            if val != -1:
                if maxi == val:
                    max_rollno.append(i + 1)
                elif maxi < val:
                    max_rollno = [i + 1]
                    maxi = val

                if mini == val:
                    min_rollno.append(i + 1)
                elif mini >= val:
                    min_rollno = [i + 1]
                    mini = val

        max_rollno, min_rollno = ', '.join(map(str, max_rollno)), ', '.join(map(str, min_rollno))

        print(f'Highest Test Score : Roll No : ({max_rollno}) with Marks = {maxi}\n')
        print(f'Lowest Test Score : Roll No : ({min_rollno}) with Marks = {mini}\n\n')


    def frequency(self):
        max_marks = 10
        freq = [0] * (max_marks + 1)
        stud, marks, index = 0, 0, []

        for val in self.fds:
            if val != -1:
                freq[val] += 1

        for i, val in enumerate(freq):
            if stud <= val:
                marks = i
                stud = val

        for i, val in enumerate(self.fds):
            if val == marks:
                index.append(i + 1)

        index = ', '.join(map(str, index))
        print(f'Maximum of {marks} marks are scored by {stud} students with Roll No: ({index})')


def main():
    test = Test()
    test.getdata()
    test.putdata()
    test.avg()
    test.absstud()
    test.maxmin()
    test.frequency()

if __name__ == "__main__":
    main()
