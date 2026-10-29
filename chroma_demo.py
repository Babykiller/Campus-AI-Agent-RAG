import os
# 加这行是为了防止国内下载 HuggingFace 模型失败
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com" 

import chromadb
from sentence_transformers import SentenceTransformer

print("1. 正在加载 Embedding 模型（首次运行会下载，请稍等）...")
model = SentenceTransformer('BAAI/bge-small-zh-v1.5')

# 你的原始资料
raw_documents = [
    "西安建筑科技大学信管专业的必修课包括数据库原理和运筹学。",
    "数据库原理的考试安排在第 16 周周四，考试形式为闭卷。",
    "运筹学的考试安排在第 17 周周一，考试形式为开卷。",
    "形势与政策课程不需要考试，提交一篇论文即可。",
    "如果对考试安排有疑问，请咨询教务处或任课老师。"
]

print("2. 正在建立本地数据库 chroma_db...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="xauat_exam_schedule")

# 向量化并存入
embeddings = model.encode(raw_documents).tolist()
ids = [f"doc_{i}" for i in range(len(raw_documents))]

collection.add(
    documents=raw_documents,
    embeddings=embeddings,
    ids=ids
)

print(f"✅ 成功！数据已存入，当前数据库共有 {collection.count()} 条数据。")