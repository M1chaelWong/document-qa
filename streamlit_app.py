import streamlit as st
import pandas as pd
import openpyxl
import requests

st.title("数据分析Demo")

# 上传Excel文件
uploaded_file = st.file_uploader(
    "上传Excel文件", type=("xlsx")
)

# 提出你的数据分析要求
question = st.text_area(
    "提出你的数据分析要求",
    placeholder="提出你的数据分析要求",
    disabled=not uploaded_file,
)




if uploaded_file and question:
    df = pd.read_excel(uploaded_file.read())
    st.dataframe(df)

    # 向aipaas发起请求生成代码
    url = "https://aipaas.dingtalk.alibaba-inc.com/bagualu/ai/generate";


    headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }

    prompt = "基于pandas写一段python代码, 将下面这个dataframe表格隔行插入空行:" +  df.to_string()
    print(prompt)


    data = {
        "productCode": "DING_DOC",
        "corpId": "ding8196cd9a2b2405da24f2f5cc6abecb85",
        "module": "OKR",
        "serviceId": "qwen-plus",
        "prompt": prompt,
        "staffId": "270771",
        "attachInfo":{ 
        },
        "monitorInfo":{   
        }
    }

    response = requests.post(url, headers=headers, json=data).json()

    


    # 目标URL
    url = "http://1487434140287185.cn-zhangjiakou.pai-eas.aliyuncs.com/api/predict/sandbox_test/execute"

    # 请求头部信息 (headers)
    headers = {
        'Authorization': 'ZDhlYTJlZDk3ZTRiNDY1MWYxYjgyN2RkOTAyZDBjYThlODI1ODAyMQ==',
        'Content-Type': 'application/json; charset=utf-8', 
        'API-KEY': 'pb-KzFcyCar93276BF5FDD6488ea5cF86d8BabA7d98RdoR2OIo', 
        'KERNEL-ID': '75501414-472f-494c-92b1-0d947790c763'
    }

    # 请求体数据
    data = {
        "code": "import requests\nimport pandas as pd\nfrom io import BytesIO\nimport matplotlib.pyplot as plt\n\n# Group by '商品二级分类' and sum the '购买数量'\ncategory_counts = df.groupby('商品二级分类')['购买数量'].sum()\n\n# Create a bar chart\ncategory_counts.plot(kind='bar', color='skyblue')\n\n# Set title and labels\nplt.title('每个商品二级分类的购买数量分布')\nplt.xlabel('商品二级分类')\nplt.ylabel('购买数量')\n\nplt.show()"
    }

    # 发起POST请求
    response = requests.post(url, headers=headers, json=data).json()
    response = response["results"][0]
    # 打印返回的响应内容
    st.markdown(f"""<img src="data:png;base64,{response["data"]}" width='500' height='500' >""", True)
    
    # image_bytes = base64.b64decode(response["data"])

    # st.write(image_bytes)





    # # Generate an answer using the OpenAI API.
    # stream = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=messages,
    #     stream=True,
    # )

    # # Stream the response to the app using `st.write_stream`.
    # st.write_stream(stream)
