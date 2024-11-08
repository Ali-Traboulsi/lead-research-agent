import json
import csv

# Load the CSV data
csv_file = 'customer_leads_agent_QA_data.csv'
json_data = []


with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        question_answer = {
            "question": row['prompt_text'],
            "answer": row['expected_response']
        }
        json_data.append(question_answer)


json_file = 'knowledge.json'
with open(json_file, 'w') as json_output:
    json.dump(json_data, json_output, indent=4)

print(f"CSV data converted to JSON and saved in {json_file}")
