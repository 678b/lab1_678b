Lab 1: Grade Evaluator and Archiver

This project is a command-line application built with Python and Bash. It reads student course grades from a CSV file, calculates the final GPA and pass/fail status, identifies assignments eligible for resubmission, and automates the archival of CSV files for future use.

Project Structure
grade-evaluator.py: Python script that processes the grades, validates inputs, calculates GPA, determines pass/fail status, and identifies assignments for resubmission.
organizer.sh: Bash script that archives the current grades.csv file, appends a timestamp, logs the operation, and prepares a new empty grades.csv for the next batch.
grades.csv: CSV file containing the course assignments, their groups, scores, and weights.
README.md: This documentation.
.gitignore: File to ignore runtime-generated files such as the archive folder and log files.
CSV File Format

The grades.csv file should have the following structure:

assignment,group,score,weight

Example:

Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20

The group column must be either Formative or Summative.
Scores must be between 0 and 100.
Formative assignments must total 60 in weight and Summative assignments must total 40 in weight.
How the Python Script Works
Prompts the user for the CSV file name.
Validates that the file exists and reads its contents into a list of dictionaries.
Checks that each score is between 0 and 100.
Validates that the total weights are correct: total weight is 100, Formative totals 60, Summative totals 40.
Calculates the final weighted grade and GPA using the formula:
GPA = (Total Grade / 100) * 5.0
Determines pass/fail status: a student passes only if they score at least 50 percent in both Formative and Summative categories.
Identifies failed Formative assignments with the highest weight as eligible for resubmission.
Prints the final grade, GPA, status, and resubmission options.
How the Bash Script Works
Checks if an archive directory exists in the project folder. If it does not, it creates it.
Generates a timestamp representing the current date and time.
Renames the existing grades.csv file by appending the timestamp and moves it to the archive folder.
Creates a new empty grades.csv file in the project folder for the next batch.
Logs the archival action with timestamp, original filename, and new filename into organizer.log.
How to Run the Project
Running the Python Script
Open CMD or terminal in the project folder.
Run the Python script:

python grade-evaluator.py

When prompted, enter the name of the CSV file:

grades.csv

The script will output the final grade, GPA, pass/fail status, and assignments eligible for resubmission.
Running the Bash Script

Since Bash scripts are not native to CMD, you need either Git Bash or WSL (Ubuntu on Windows).

Using Git Bash:
Right-click in the project folder and select Git Bash Here.
Run the script:

bash organizer.sh

The script will archive grades.csv, create a new empty grades.csv, and update organizer.log.
