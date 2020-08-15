# regular expression
# 정규식 : 정해진 형태를 의미하는 식

import re
# 만약 4자리의 문자 조합이 있다고 가정할 때
# 현재 나는 세자리 정도만 기억을 하고 있는 상태이다.
# 그러면 어떤식으로 원래의 문자를 찾을 수 있을까?
# ca?e => cafe, cabe, cave, care ...

p = re.compile("ca.e")  # 하나의 문자를 의미하는 문자열을 컴파일하고 패턴 값을 받음

# . (ex: ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (ex: ^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (ex: se$) : 문자열의 끝 > case, base (o) | face (x)

# 받은 패턴과 매칭되는지를 확인
# m = p.match("case")
# # print(m.group()) # 매치되지 않으면 에러가 발생
# if m:
#     print(m.group())
# else:
#     print("매칭되지 않음")

# if문을 함수로 만들어 재사용 가능성 있게 만들어 보자.


def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string():", m.string)  # 입력받은 문자열 (string은 함수가 아니라 변수)
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.end():", m.end())  # 일치하는 문자열의 끝 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


# m = p.match("case")  # match : 주어진 문자열의 처음부터 일치하는지 확인
# # 그래서 careless 같은 경우도 일치된다.
# print_match(m)

# m = p.search("good case")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로 변환
print(lst)

# 참고 레퍼런스 : https://www.w3schools.com/python/python_regex.asp
#              https://docs.python.org/ko/3/library/re.html
