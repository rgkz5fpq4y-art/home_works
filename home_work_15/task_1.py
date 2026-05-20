class GroupLimitError(Exception):
    def __init__(self, message='В групi не може бути бiльше 10 студентiв!'):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} years old, {self.gender} "

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age,first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()} {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students}'


if __name__ == '__main__':
        gr = Group("PD11")
        try:
            for i in range(11):
                st = Student("Male", 20+i, f'Name{i}', f'LastName{i}', f'ID{i}')
                print(f"Try to add: {st.first_name} {st.last_name}")
                gr.add_student(st)
        except GroupLimitError as e:
            print(f"\n[Помилка перехоплена]: {e}")

        print("\nВсього в групi:")
        print(gr)


