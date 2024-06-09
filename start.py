import os

base_path = '/home/xlab-app-center/.cache/model'
# base_path = './model'
os.system(f'git clone https://code.openxlab.org.cn/OpenLMLab/internlm2-chat-1.8b.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
# file_path = '/home/xlab-app-center/.cache/files'
# file_path = './files'
# os.system(f'cd ..')
# os.system(f'git clone https://github.com/bitEEdh/LLM-assistant-for-Commun.git {file_path}')
# os.system(f'python {file_path}/RAG_init.py')
# os.system(f'cd {file_path}')
os.system(f'python RAG_init.py')
os.system(f'streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')

# import os
# import subprocess

# base_path = '/home/xlab-app-center/.cache/model'
# # base_path = './model'

# # Clone the repository into base_path
# try:
#     subprocess.run(['git', 'clone', 'https://code.openxlab.org.cn/OpenLMLab/internlm2-chat-1.8b.git', base_path], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error during git clone: {e}")
#     raise

# # Pull LFS files
# try:
#     subprocess.run(['git', 'lfs', 'pull'], cwd=base_path, check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error during git lfs pull: {e}")
#     raise

# file_path = '/home/xlab-app-center/.cache/files'
# # file_path = './files'

# # Clone the second repository into file_path
# try:
#     subprocess.run(['git', 'clone', 'https://github.com/bitEEdh/LLM-assistant-for-Commun.git', file_path], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error during git clone: {e}")
#     raise

# # Run the Python script
# try:
#     subprocess.run(['python', f'{file_path}/RAG_init.py'], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error running RAG_init.py: {e}")
#     raise

# # Start the Streamlit app
# try:
#     subprocess.run(['streamlit', 'run', f'{file_path}/web_demo.py', '--server.address=0.0.0.0', '--server.port=7860'], check=True)
# except subprocess.CalledProcessError as e:
#     print(f"Error starting Streamlit: {e}")
#     raise
