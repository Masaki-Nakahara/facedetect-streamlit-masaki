import streamlit as st
from PIL import Image   #画像の読み取り
import cv2  #opencvのimport 
import numpy as np
import pyocr
import pyocr.builders





st.title('画像分別アプリ')



uploaded_file = st.file_uploader('判別したい画像の選択', type = 'jpg')

if uploaded_file is not None:   #画像があれば


    image = Image.open(uploaded_file)
    img_array = np.array(image, dtype=np.uint8)
    st.image(img_array,caption = '元画像',use_column_width = None)

    tools = pyocr.get_available_tools()
    tool = tools[0]
    langs = tool.get_available_languages()

    txt = tool.image_to_string(
        image,
        lang='jpn',
        builder=pyocr.builders.TextBuilder()
    )

      
    if len(txt) >= 20:
        st.image(img_array, caption = '文字検出', use_column_width = True)
        st.write('検出した文字')
        st.write(txt)
    else:        
        color = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        xml_path = '/Users/nakaharamizuki/python/人工知能/haarcascades/haarcascade_frontalface_alt.xml' #カスケード分類器のモデルがあるファイルのパスの指定
        classifier = cv2.CascadeClassifier(xml_path)    #ファイルのパスを元にカスケード分類器を作成
        targets = classifier.detectMultiScale(color)    #カスケード分類器を適応し，顔を認識したx座標，y座標，幅，高さの値をtargetsにリスト型で格納

        for x, y, w, h in targets:
            cv2.rectangle(img_array, (x, y), (x + w, y + h), (255, 0, 0), 2) 


        if len(targets) != 0:   #targetsが空ではない，つまり顔が一つでも認識されたら，ファイルをhumanに格納
            st.image(img_array, caption = '顔検出', use_column_width = True)
            st.write('検出した人数')
            st.write(len(targets))
        else:
            st.write('顔なし')