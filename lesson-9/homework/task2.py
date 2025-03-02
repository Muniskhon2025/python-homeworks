import csv
from collections import defaultdict

def read_grades(filename):
    grades = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  # Convert grade to integer
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = defaultdict(list)
    for entry in grades:
        subject_totals[entry['Subject']].append(entry['Grade'])
    
    subject_averages = {subject: sum(grades) / len(grades) for subject, grades in subject_totals.items()}
    return subject_averages

def write_average_grades(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

def main():
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'
    
    grades = read_grades(input_file)
    averages = calculate_average(grades)
    write_average_grades(output_file, averages)
    print("Average grades calculated and written to", output_file)

if __name__ == "__main__":
    main()
