import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Dataframe')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

#データフレーム表示
#st.write(df)

#データフレームを指定サイズで表示（スクロールバー付き）
#st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

#データフレームの表示（静的なテーブルを表示するときに使う、ソートができない）
st.table(df.style.highlight_max(axis=0))

# マークダウン記法で記述
"""
# 章
## 節
### 項

```
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df2) #折れ線グラフ
st.area_chart(df2) #面積グラフ
st.bar_chart(df2) #棒グラフ

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat','lon']
)
st.map(df3) #地図表示

st.write('Display Imege')
if st.checkbox('Show Image'):
    img = Image.open('image\sample.jpg')
    st.image(img, caption='sample_test', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は', option ,'です' #st.writeを使わなくても表示できる

option2= st.text_input('あなたの趣味を教えてください')
'あなたの趣味:', option2 #st.writeを使わなくても表示できる

option3 = st.slider('あなたの今の調子は？',0,100,50)
'あなたの調子:', option3 #st.writeを使わなくても表示できる

#サイドバーに表示
#sidebarを使うだけで表示位置をサイドバーに持っていくことができる

#左右のレイアウト配置を可能にする
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです')

#クリックすると詳細が開く形式
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#プログレスバーの表示
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i)
    time.sleep(0.1)


