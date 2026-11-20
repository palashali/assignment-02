def format_number(value: float) -> str:
    """Format whole numbers without trailing .0, and decimals to 2 places."""
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}"


def main() -> None:
    student_name = input("Enter student name: ").strip()

    subject_1 = float(input("Enter marks for Subject 1: "))
    subject_2 = float(input("Enter marks for Subject 2: "))
    subject_3 = float(input("Enter marks for Subject 3: "))

    total_marks = subject_1 + subject_2 + subject_3
    average_marks = total_marks / 3

    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "F"

    summary = (
        f"\nStudent Name: {student_name}\n"
        f"Total Marks: {format_number(total_marks)}\n"
        f"Average: {average_marks:.2f}\n"
        f"Grade: {grade}"
    )
    print(summary)


if __name__ == "__main__":
    main()
