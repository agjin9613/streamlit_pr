# 유저한테 숫자, 문자, 시간, 색을 입력받는 방법

import streamlit as st

def main():
    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요!')

    st.text(name + '안녕하세요??')

    # 2. 입력 글자 갯수 제한
    address = st.text_input("주소를 입력하세요", max_chars=10)
    st.text(address)

    # 3. 여러 행을 입력 가능하도록
    message = st.text_area('메세지를 입력하세요.', height=3)
    st.text(message)

    # 4. 비밀번호 입력 (12글자까지)
    password = st.text_input('비밀번호를 입력하세요', max_chars=12, type='password')
    st.text(password)

    # 5. 정수 입력하는 방법
    integer_input = st.number_input('정수를 입력하세요', min_value=-10, max_value=100, step=1)

    # 6. 실수 입력하는 방법
    float_input = st.number_input('실수를 입력하세요', min_value=-5.3, max_value=10.8, step=0.5)

    # 7. 날짜 입력하는 방법
    my_date = st.date_input('약속 날짜 선택')
    st.write(my_date)

    # 8. 요일 찍기
    st.text(my_date.strftime('%A'))

    # 9. 시간 입력 받는 방법
    my_time = st.time_input('시간 선택')
    st.write(my_time)
    st.write(my_time.strftime('%H:%M'))

    # 10. 색상 선택
    color = st.color_picker('색을 선택하세요')
    st.write(color)


if __name__ == '__main__':
    main()