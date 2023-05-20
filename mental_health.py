# import csv
# import re

# unwanted_questions = ["If 'Other' please specify (for general health conditions)",
#                       "Mental Health Problems - Other",
#                       "Trauma - Other",
#                       "Caregiver Support - Other","Do you currently have health insurance?"]

# # Read the CSV file
# with open('mental_health.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     rows = list(reader)

# # Remove the unwanted questions and numbers from the rows
# modified_rows = []
# for row in rows:
#     question = row[0]
#     print(question)
#     question_without_number = re.sub(r"^\d+\.\s*", "", question)  # Remove the number and the dot from the beginning of the question
#     question_without_quotes = question_without_number.replace('"','')  # Remove the surrounding double quotes
#     if question_without_quotes not in unwanted_questions:
#         modified_rows.append([question_without_quotes])
    
# # Write the modified rows back to the CSV file
# with open('mental_health.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(modified_rows)

