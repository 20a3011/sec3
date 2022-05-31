import streamlit as st
import time

st.snow()

st.title('Streamlit 入門')

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!!'

if st.checkbox('Show Text'):
    st.write('DataFrame')

"""
# 章
## 節
### 項

```python
import streamlit as st
```
"""

option = st.selectbox(
    'あなたの好きな数字を選んで下さい',
    list(range(1,11))
)
'あなたの好きな数字は', option, 'です。'

text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味 : ', text

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション : ', condition

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('此処は右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')