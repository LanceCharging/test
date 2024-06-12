"""
엿같은 거,

inspect.getsource
이것도 주피터 노트북에선 안 먹히네
되는 게 뭐야
"""

import inspect


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}이고, {self.age}살입니다.")


# Person 클래스를 상속하는 Student 클래스
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 클래스의 초기화 메서드 호출
        self.student_id = student_id

    def introduce(self):
        super().introduce()  # 부모 클래스의 introduce 메서드 호출
        print(f"제 학번은 {self.student_id}입니다.")


print(inspect.getsource(Student))
