import streamlit as st
import google.generativeai as genai
import os

# 1. API 키 설정 (아래 따옴표 안에 선생님이 발급받은 열쇠를 붙여넣으세요)
API_KEY = os.environ.get("GOOGLE_API_KEY", "AQ.Ab8RN6JULjgvJte0vyS6uVUmUd_8xDdH6UdPOCHS8d6f4lHHHg")
genai.configure(api_key=API_KEY)

# 2. 덕배 할아버지 설정 지시문
system_instruction = """
너는 초등학교 3학년 학생들과 대화하는 '덕배 할아버지'야. 
동네 30년 토박이이며, 다리가 불편해 지팡이를 짚고 다녀. 
아이들에게 동네의 옛 모습과 지금 모습을 다정하게 들려주고, 생활 속 불편함에 대해 이야기해줘.
초등학교 3학년 수준의 아주 쉬운 단어와 짧은 문장(2~3문장)만 사용하고, 외국인 학생도 이해할 수 있도록 직관적으로 말해. 
대화 끝에는 아이들이 배려와 살기 좋은 마을에 대해 스스로 생각할 수 있는 쉬운 질문을 던져줘. 
장난을 치면 부드럽게 동네 이야기로 넘어가.
"""

# 3. 인공지능 두뇌 연결 (Gemini)
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=system_instruction
)

# 4. 2030 교실 태블릿용 화면 디자인
st.set_page_config(page_title="덕배 할아버지와 대화하기", page_icon="👴")
st.title("👴 덕배 할아버지와 대화하기")
st.subheader("우리 고장에 대해 궁금한 것을 여쭤보세요!")

# 대화 기록 저장
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

for message in st.session_state.chat_session.history:
    if message.role == "user":
        with st.chat_message("user", avatar="👦"):
            st.write(message.parts[0].text)
    else:
        with st.chat_message("assistant", avatar="👴"):
            st.write(message.parts[0].text)

# 5. 학생 질문 입력 칸
user_input = st.chat_input("할아버지에게 하고 싶은 말을 적어보세요.")

if user_input:
    # 학생의 질문을 화면에 띄우기
    with st.chat_message("user", avatar="👦"):
        st.write(user_input)
    
    # 덕배 할아버지의 대답을 화면에 띄우기
    with st.chat_message("assistant", avatar="👴"):
        response = st.session_state.chat_session.send_message(user_input)
        st.write(response.text)
