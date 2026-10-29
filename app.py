import os
os.environ["HF_HUB_OFFLINE"] = "1"  # 强制开启离线模式，禁止联网检查更新
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os

print("🚀 网页开始加载...")

st.set_page_config(page_title="我的专属校园 AI", page_icon="🤖")
st.title("🤖 我的专属校园 AI 助手")
st.caption("基于 RAG 架构与 DeepSeek 大模型开发")

@st.cache_resource
def load_models():
    print("⏳ 开始加载 Embedding 模型（这步可能很慢）...")
    embed_model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
    print("✅ 模型加载成功！")
    
    print("⏳ 开始连接 ChromaDB 数据库...")
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="xauat_exam_schedule")
    print("✅ 数据库连接成功！")
    
    return embed_model, collection

# 尝试加载模型
try:
    embed_model, collection = load_models()
except Exception as e:
    st.error(f"加载出错啦！错误信息：{e}")
    print(f"❌ 报错: {e}")
    st.stop()

# 为了让页面不黑屏，先写一个测试文字
st.write("👋 如果你看到这句话，说明界面渲染成功！")

# ... 下面是你原来的侧边栏和聊天逻辑 ...
with st.sidebar:
    st.header("设置")
    api_key = st.text_input("请输入 DeepSeek API Key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("请输入你的问题，比如：运筹学什么时候考？"):
    if not api_key:
        st.error("请先在左侧设置中输入 API Key！")
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("正在查阅本地资料库..."):
        query_embedding = embed_model.encode([prompt]).tolist()
        results = collection.query(query_embeddings=query_embedding, n_results=2)
        context = "\n".join(results['documents'][0])
        
        llm_prompt = f"""请根据以下资料回答问题。如果资料中没有答案，请如实说“资料库中未找到相关信息”。
        
资料：
{context}

问题：{prompt}
"""

    with st.chat_message("assistant"):
        with st.spinner("AI 正在思考..."):
            client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": llm_prompt}]
            )
            answer = response.choices[0].message.content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})