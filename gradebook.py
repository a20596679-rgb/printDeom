# 평균을 계산하는 함수
def mean(scores):
    # 평균을 계산할 경우 0으로 처리
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# 평균 점수에 따라 학점을 결정하는 함수
def get_letter_grade(score): # 'score'는 단일 평균 점수여야 함
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 한 명의 학생 정보를 저장하는 클래스
class Student:
    # 학생의 '이름'과 '점수들'을 저장
    def __init__(self, name, scores):
        self.name = name     # 학생 이름
        self.scores = scores # 학생의 점수 리스트

    # 평균 계산
    def get_average(self):
        return mean(self.scores)

    # 학점 계산
    def get_grade(self):
        # get_letter_grade 함수에 'get_average()'로 계산한 단일 평균 점수를 전달
        return get_letter_grade(self.get_average())

# 여러 학생의 성적을 관리하는 클래스
class GradeBook:
    def __init__(self):
        self.students = [] # 학생들을 저장할 리스트

    # 학생 추가
    def add_student(self, student):
        self.students.append(student)

    # 전체 반 평균 계산
    def class_average(self):
        total = 0
        for s in self.students:
            # FIX: 학생 객체 's'의 평균을 가져오기 위해 'get_average()' 메서드를 호출해야 함
            total += s.get_average()
        
        # 학생들이 없을 경우 0을 반환하여 ZeroDivisionError 방지
        if not self.students:
            return 0
            
        return total / len(self.students)

# 프로그램의 시작 부분 (main 함수)
def main():
    # 학생 객체 생성
    alice = Student("Alice", [90, 85, 82])
    bob = Student("Bob", [78, 75, 68])

    # 성적표를 관리할 학생 추가
    gb = GradeBook()
    gb.add_student(alice)
    gb.add_student(bob)

    # 전체 반 평균 출력
    print(f"전체 반 평균 점수: {round(gb.class_average(), 2)}")
    print("-" * 30)

    # 각 학생의 평균과 학점 출력
    for s in gb.students:
        # 평균과 학점 출력 시 f-string 사용
        print(f"학생({s.name}): 평균: {round(s.get_average(), 1)}점, 학점: {s.get_grade()}")

# 프로그램 시작
if __name__ == "__main__":
    main()
