import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("📊 가장 쉬운 Streamlit 앱")
st.write("✅ Streamlit은 이렇게 간단하게 시작할 수 있어!")
name = st.text_input("이름을 입력해보세요:")
if name:
    st.success(f"환영합니다, {name}님!")


st.title("📊 간단한 Streamlit 대시보드")

# 예제 데이터 생성
data = pd.DataFrame({
    '날짜': pd.date_range(start='2023-01-01', periods=10),
    '판매량': np.random.randint(20, 100, size=10),
    '매출': np.random.randint(1000, 5000, size=10)
})

st.write("## 판매 데이터")
st.dataframe(data)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(data['날짜'], data['판매량'], marker='o', label='판매량')
ax.set_xlabel('날짜')
ax.set_ylabel('판매량')
ax.set_title('날짜별 판매량 추이')
ax.legend()

st.pyplot(fig)