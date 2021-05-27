import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

st.write('DataFrame')

st.write('プログレスバーの表示')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_colum, right_column = st.beta_columns(2)
button = left_colum.button('右からむにぼたん')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('回答１')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('回答２')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('回答３')
# text = st.text_input('あなたの趣味は？')
# condision = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は', text, 'です。'
# 'コンディション',condision
# option = st.selectbox(
#     '好きな数字は？',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('pic.jpg')
#     st.image(img,caption='FUKEI',use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.map(df)

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )

# st.bar_chart(df)

# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
# })



# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """