import os

base_path = './models'
os.system(f'git clone https://code.openxlab.org.cn/OpenLMLab/internlm2-chat-1.8b.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
file_path = './files'
os.system(f'git clone https://github.com/bitEEdh/LLM-assistant-for-Commun.git {file_path}')
os.system(f'python {file_path}/RAG_init.py')
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')
