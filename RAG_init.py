from RAG.VectorBase import VectorStore
from RAG.utils import ReadFiles
from RAG.LLM import InternLMChat
# from RAG.Embeddings import JinaEmbedding
from RAG.Embeddings import BgeEmbedding
import os

# 没有保存数据库
if not os.path.isdir('/home/xlab-app-center/.cache/storage'):
    docs = ReadFiles('dataset').get_content(max_token_len=600, cover_content=150) # 获得data目录下的所有文件内容并分割
    embedding = BgeEmbedding()
    vector = VectorStore(docs)
    vector.get_vector(EmbeddingModel=embedding)
    vector.persist(path='/home/xlab-app-center/.cache/storage') # 将向量和文档内容保存到storage目录下，下次再用就可以直接加载本地的数据库
# 使用保存好的数据库
else:
    vector = VectorStore()
    vector.load_vector('/home/xlab-app-center/.cache/storage') # 加载本地的数据库
    embedding = BgeEmbedding()

# question = 'What is the reason for including sequence numbers in each packet encapsulated within a GRE-based Layer 3 overlay tunnel? Choose from the following options: A. To enable host mobility. B. To support Network Ingress Filtering. C. To prevent TCP collapse. D. To load-balance packets over different access networks. Before you choose an option, list the thinking process and give the reason of your choice.'
# question = 'What is the reason for including sequence numbers in each packet encapsulated within a GRE-based Layer 3 overlay tunnel?'
# question = 'What are possible mechanisms that can be used to transform data into an unintelligible form?'
# question = 'Which mechanism is used to transform data into an unintelligible form?'

# content = vector.query(question, EmbeddingModel=embedding, k=1)[0]
def process_user_input(question: str) -> str:
    context = vector.query(question, EmbeddingModel=embedding, k=1)[0]
    prompt = f"""Use the provided context to answer the user's question. If you do not know the answer, say that you do not know. Always respond in English.
        The user's question is: {question}
        Available context:
        ···
        {context}
        ···
        If the given context does not provide enough information for you to answer, please respond that the content is not in the database and you do not know.
        The user's question is: {question}
        Useful answer:"""
    return prompt

# chat = OpenAIChat(model='gpt-3.5-turbo-1106')
# chat = InternLMChat(path='/root/RAG/TinyRAG/models/internlm2-chat-1_8b')

# print(chat.chat(question, [], content),'\n')
# print(content)
