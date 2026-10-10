
# Student Marks Data Analysis
# Beginner Data Analysis Project

def main():
    print("===== Student Marks Data Analysis =====")

    students = []

    while True:
        name = input(
            "\nEnter student name (or type 'done' to finish): "
        ).strip()

        if name.lower() == "done":
            break

        if not name:
            print("Name cannot be empty.")
            continue

        try:
            marks = float(input("Enter marks (0-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            continue

        students.append({"name": name, "marks": marks})

    if not students:
        print("No data entered. Please run the program again.")
        return

    marks_list = [student["marks"] for student in students]

    average = sum(marks_list) / len(marks_list)
    highest = max(students, key=lambda s: s["marks"])
    lowest = min(students, key=lambda s: s["marks"])

    print("\n===== Analysis Report =====")
    print(f"Number of students: {len(students)}")
    print(f"Average marks: {average:.2f}")
    print(f"Highest: {highest['name']} ({highest['marks']:g})")
    print(f"Lowest: {lowest['name']} ({lowest['marks']:g})")

    print("\n===== Marks Chart =====")
    for student in students:
        bar_length = int(student["marks"] // 2)
        bar = "#" * bar_length
        print(f"{student['name'][:15]:15} | {bar} "
              f"{student['marks']:g}")

    passed = sum(1 for mark in marks_list if mark >= 50)
    failed = len(students) - passed

    print("\n===== Summary =====")
    print(f"Passed (50 or above): {passed}")
    print(f"Below 50 marks: {failed}")


if __name__ == "__main__":
    main()
