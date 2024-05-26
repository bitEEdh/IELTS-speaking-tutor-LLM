import json

# Function to read the JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write to a JSON file
def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to replicate each item in the dataset 100 times
def replicate_items(data, times=1000):
    replicated_data = []
    for item in data:
        replicated_data.extend([item] * times)
    return replicated_data

# Main function to perform the task
def main(input_file_path, output_file_path):
    # Read the original data
    original_data = read_json_file(input_file_path)
    
    # Replicate each item 100 times
    new_data = replicate_items(original_data)
    
    # Write the new data to the output file
    write_json_file(new_data, output_file_path)
    print(f"New JSON file created with {len(new_data)} items.")

# Define the input and output file paths
input_file_path = 'e:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\python_scripts\instruction_ft_dataset\TeleQnA_Research_overview_first_10_instruction_ft.json'
output_file_path = 'e:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\python_scripts\instruction_ft_dataset\TeleQnA_Research_overview_first_10_replicate_1000_instruction_ft.json'

# Run the main function
main(input_file_path, output_file_path)
