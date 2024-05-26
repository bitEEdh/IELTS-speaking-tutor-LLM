'''
功能：word文档《项目笔记》中的“提示词 2”的功能
'''
import json

def transform_data(input_file, output_file):
    # Read the input data from the text file
    with open(input_file, 'r') as file:
        data = file.read()
    
    # Split the data into individual question-answer pairs
    qa_pairs = data.strip().split('\n\n')
    
    # Initialize a list to hold the transformed data
    transformed_data = []
    
    # Process each question-answer pair
    for pair in qa_pairs:
        # Parse the question-answer pair as a JSON object
        qa = json.loads(pair)
        
        # Extract the explanation
        explanation = qa["explanation"]
        
        # Create the new format
        new_format = {
            "conversation": [
                {
                    "system": "",
                    "input": "",
                    "output": explanation
                }
            ]
        }
        
        # Add the new format to the list
        transformed_data.append(new_format)
    
    # Write the transformed data to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(transformed_data, file, indent=4)

# Define the input and output file paths
input_file = 'e:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\python_scripts\TeleQnA_Research_overview.txt'
output_file = 'TeleQnA_Research_overview_pretrain.json'

# Call the function to transform the data
transform_data(input_file, output_file)
