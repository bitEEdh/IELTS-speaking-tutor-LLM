import os

base_path = '/home/xlab-app-center/.cache/model'
# base_path = './model'
os.system(f'git clone https://code.openxlab.org.cn/OpenLMLab/internlm2-chat-1.8b.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
file_path = '/home/xlab-app-center/.cache/files'
# file_path = './files'
# os.system(f'cd ..')
os.system(f'git clone https://github.com/bitEEdh/LLM-assistant-for-Commun.git {file_path}')
os.system(f'python {file_path}/RAG_init.py')
# os.system(f'cd {file_path}')
os.system(f'streamlit run {file_path}/web_demo.py --server.address=0.0.0.0 --server.port 7860')
