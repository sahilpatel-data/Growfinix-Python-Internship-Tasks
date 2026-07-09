import argparse
import re
import csv


def extract_email(text):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


def extract_name(text):
    name_patterns = [
        r'my name is ([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?=\.|,| and| I want|$)',
        r'this is ([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?=\.|,| here| I am|$)',
        r'Name\s*[:\-]\s*([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?=\.|,|$)',
        r'I[’\']?m ([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?= and|\.|,|$)',
        r'from ([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?= for|\.|,|$)',
        r'Myself ([A-Z][a-z]+(?: [A-Z][a-z]+)+?)(?=\.|,|$)'
    ]

    for pattern in name_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Not Found"


def extract_destination(text):
    destination_patterns = [
        r'trip to ([A-Za-z ]+?)(?: next month| next week| soon|\.|,|$)',
        r'package for ([A-Za-z ]+?)(?:\.|,|$)',
        r'Destination\s*[-:]\s*([A-Za-z ]+?)(?:\.|,|$)',
        r'package to ([A-Za-z ]+?)(?:\.|,|$)',
        r'for ([A-Za-z ]+?) vacation',
        r'interested in ([A-Za-z ]+?) trip'
    ]

    for pattern in destination_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Not Found"


def parse_enquiries(file_path, output_file):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    enquiries = [entry.strip() for entry in content.split("\n\n") if entry.strip()]

    if not enquiries:
        print("No enquiries found in the file.")
        return

    extracted_data = []

    print("\n===== CLEANED TOUR ENQUIRY SUMMARY =====\n")

    for index, enquiry in enumerate(enquiries, start=1):
        name = extract_name(enquiry)
        email = extract_email(enquiry)
        destination = extract_destination(enquiry)

        extracted_data.append([index, name, email, destination])

        print(f"Enquiry {index}")
        print(f"Name       : {name}")
        print(f"Email      : {email}")
        print(f"Destination: {destination}")
        print("-" * 50)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Enquiry No", "Name", "Email", "Destination"])
        writer.writerows(extracted_data)

    print(f"\nCleaned data has also been saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="CLI Log Parser for Tour Enquiries")
    parser.add_argument("file", help="Path to the raw tour enquiry text file")
    parser.add_argument(
        "--output",
        default="cleaned_enquiries.csv",
        help="Output CSV file name (default: cleaned_enquiries.csv)"
    )

    args = parser.parse_args()

    parse_enquiries(args.file, args.output)


if __name__ == "__main__":
    main()