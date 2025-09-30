# Python 실습 예제 설명

이 문서는 Python의 다양한 기능을 실습하는 예제 파일에 대한 설명입니다.


## 파일 목록

### 1) `main_print_v1.py`
- **설명**: 표준 `print()` 활용 예제
- **동작/기능**
    - 기본출력, 여러값 출력(`sep`, `end`)
    -f-string / `str.format()` / C 스타일 `%` 포맷
    -딕셔너리 출력, 멀티라인 출력(`\`, 삼중따옴표)
    -간단한 계산/함수 호출을 포함한 f-string

---

### 2) `main_print_v2.py`
- **설명**: 콘솔을 보기 좋게 꾸미기 위해 `rich` 라이브러리를 사용하는 예제
- **동작/기능**
    - 컬러/스타일 텍스트 출력 (`rich.print`)
    - `panel` 로 박스형 멀티라인 출력
    - `Table` 로 딕셔너리/레코드 출력
    - `sep`, `end` 옵션 조합
- **실행 전 준비**: `pip install rich`

---

### 3) `main_print_v1.ipynb`
- **설명**: `main_print_v1.py` 파일을 jupyter로 변환한 파일

---

### 4) `requirements.txt`
- **설명**: `main_print_v2.py`에서 실습했던 pip환경을 다른사람과 공유하기 위해 사용자의 pip환경을 txt파일로 저장한 파일