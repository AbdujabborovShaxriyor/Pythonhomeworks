import csv

def read_file(file_name):
    grades = []
    with open(file_name,"r",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({subject: int(score) for subject, score in row.items()})
    return grades

def write_file(grades):
    subject_totals = {}
    subject_counts = {}
    for row in grades:
        for subject, score in row.items():
            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0
            subject_totals[subject] += score
            subject_counts[subject] += 1

    averages = {subject: round(subject_totals[subject] / subject_counts[subject], 2) for subject in subject_totals}
    return averages

def write_averages(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])  
        for subject, avg in averages.items():
            writer.writerow([subject, avg])
            
def main():
    input_file = "grades.csv"
    output_file = "average_grades.csv"

    grades = read_file(input_file)
    averages = write_file(grades)
    write_averages(output_file, averages)

    print("Average grades written to", output_file)


if __name__ == "__main__":
    main()