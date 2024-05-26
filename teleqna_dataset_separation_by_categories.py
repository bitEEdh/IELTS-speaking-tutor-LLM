import json
from collections import defaultdict

# Step 1: Read the input file
input_file = 'E:\sync_files\BaiduSyncdisk\同步文件夹\竞赛和实习\书生大模型课程\project\TeleQnA\TeleQnA.txt'
with open(input_file, 'r', encoding='utf-8') as file:
    data = file.read()

# Step 2: Parse the content
# Assuming the input file contains a JSON object of question-answer pairs
try:
    questions_data = json.loads(data)
except json.JSONDecodeError:
    raise ValueError("The input file is not a valid JSON file")

# Step 3: Categorize the data
categorized_data = defaultdict(list)

for key, question_info in questions_data.items():
    category = question_info.get('category', 'Uncategorized')
    categorized_data[category].append(question_info)

# Step 4: Write to separate files
for category, questions in categorized_data.items():
    output_file = f"TeleQnA_{category.replace(' ', '_')}.txt"
    with open(output_file, 'w') as file:
        for question in questions:
            # Formatting each question-answer pair as a JSON object in the output file
            json.dump(question, file, indent=4)
            file.write('\n\n')  # Adding new lines for better readability

print("The dataset has been divided into separate files based on categories.")
