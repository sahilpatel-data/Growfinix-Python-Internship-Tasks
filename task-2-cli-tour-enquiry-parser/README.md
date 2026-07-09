```md
# Task 2 - CLI Log Parser for Tour Enquiries

## Project Overview
This project is a Python-based Command Line Interface (CLI) tool developed as part of the Growfinix Python Internship.

The tool reads a messy text file containing raw tour enquiries and uses Regular Expressions (Regex) to extract important customer details such as:
- Name
- Email Address
- Travel Destination

The cleaned data is displayed in the terminal and also exported into a CSV file for structured use.

---

## Objective
The objective of this project is to automate the extraction of useful information from unstructured tour enquiry text data.

---

## Technologies Used
- Python
- argparse
- re (Regular Expressions)
- csv

---

## Features
- Reads raw enquiry data from a text file
- Extracts customer names from multiple text patterns
- Extracts email addresses using regex
- Extracts destinations from different enquiry formats
- Displays cleaned output in the terminal
- Exports cleaned data into a CSV file
- Supports custom output CSV file using CLI argument

---

## Project Structure

```text
task-2-cli-tour-enquiry-parser/
├── parser.py
├── enquiries.txt
├── cleaned_enquiries.csv
├── README.md
└── output_sample.txt

---

## Input File
The input file `enquiries.txt` contains messy tour enquiry records written in different sentence styles.

Example:
- "Hello, my name is Rahul Sharma. I want to book a trip to Goa next month..."
- "Greetings! Name: Arjun Verma. Destination - Kashmir..."
- "Tour enquiry from Mohit Bansal for Dubai vacation..."

---

## How the Script Works
1. Accepts the input file path from the command line
2. Reads the raw enquiry text file
3. Splits the file into separate enquiry blocks
4. Uses regex patterns to extract:
   - Name
   - Email
   - Destination
5. Prints the cleaned enquiry summary in the terminal
6. Saves the cleaned output into a CSV file

---

## How to Run the Project

### Run with default output file

python parser.py enquiries.txt

This will generate:
cleaned_enquiries.csv

### Run with custom output file

python parser.py enquiries.txt --output my_enquiries.csv

---

## Author
Sahil Patel