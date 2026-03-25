import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    total_grade = 0
    formative_score = 0
    summative_score = 0

    failed_formatives = []

    # a) Validate scores and calculate totals
    for item in data:
        score = item['score']
        weight = item['weight']
        group = item['group']

        # Score validation
        if score < 0 or score > 100:
            print("Error: Invalid score detected.")
            return

        total_weight += weight

        if group == "Formative":
            formative_weight += weight
        elif group == "Summative":
            summative_weight += weight

        # Weighted score
        weighted = (score * weight) / 100
        total_grade += weighted

        if group == "Formative":
            formative_score += weighted
            if score < 50:
                failed_formatives.append(item)

        elif group == "Summative":
            summative_score += weighted

    # b) Validate weights
    if total_weight != 100:
        print("Error: Total weight must be 100.")
        return

    if formative_weight != 60:
        print("Error: Formative weight must be 60.")
        return

    if summative_weight != 40:
        print("Error: Summative weight must be 40.")
        return

    # c) GPA calculation
    GPA = (total_grade / 100) * 5.0

    # d) Pass/Fail condition
    formative_percent = (formative_score / 60) * 100
    summative_percent = (summative_score / 40) * 100

    if formative_percent >= 50 and summative_percent >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    # f) Print results
    print(f"\nFinal Grade: {round(total_grade, 2)}%")
    print(f"GPA: {round(GPA, 2)}")
    print(f"Status: {status}")

    # e) Resubmission logic
    if status == "FAILED" and failed_formatives:
        max_weight = max(a['weight'] for a in failed_formatives)

        print("\nAssignments eligible for resubmission:")
        for a in failed_formatives:
            if a['weight'] == max_weight:
                print("-", a['assignment'])


if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)