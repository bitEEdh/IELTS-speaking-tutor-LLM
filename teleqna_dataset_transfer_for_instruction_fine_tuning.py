import json
import re

def process_qa_pair(qa_pair):
    question = qa_pair["question"]
    options = [qa_pair[f"option {i}"] for i in range(1, 6) if f"option {i}" in qa_pair]
    options_str = "; ".join(options)
    
    # Extract the answer text without the "option xx:" part using regex
    answer_match = re.match(r"option \d+: (.*)", qa_pair["answer"])
    if answer_match:
        answer = answer_match.group(1)
    else:
        answer = qa_pair["answer"]

    explanation = qa_pair["explanation"]
    
    # Create the formatted dictionary as specified
    formatted_qa = {
        "conversation": [
            {
                "system": "You are an AI assistant with expertise in the field of telecommunications.",
                "input": f"{question} Choose from the following options: {options_str}. Give the chosen option and explain why it is the correct answer.",
                "output": f"{answer}. {explanation}"
            }
        ]
    }
    
    return formatted_qa

def read_and_parse_json_objects(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    # Split content into chunks based on double newlines
    json_chunks = content.strip().split('\n\n')
    
    parsed_qa_pairs = []
    for chunk in json_chunks:
        try:
            qa_pair = json.loads(chunk)
            parsed_qa_pairs.append(qa_pair)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in chunk: {chunk}\nError: {e}")
    
    return parsed_qa_pairs

def main():
    input_file = "e:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\python_scripts\TeleQnA_Research_overview.txt"  # Define the input file path
    output_file = "e:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\python_scripts\instruction_ft_dataset\TeleQnA_Research_overview_instruction_ft.json"  # Define the output file path
    
    # Read and parse the input file
    qa_pairs = read_and_parse_json_objects(input_file)
    
    # Process each parsed question-answer pair
    formatted_data = [process_qa_pair(qa_pair) for qa_pair in qa_pairs]
    
    # Write the formatted data to the output JSON file
    with open(output_file, "w") as outfile:
        json.dump(formatted_data, outfile, indent=4)
    
    print("Data transformation completed successfully.")

if __name__ == "__main__":
    main()
