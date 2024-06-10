#!/usr/bin/env python3

# Import necessary modules
import os
import datetime
import reports
import emails

# Define function to read text files and return formatted description
def get_description(file_path):
    """Reads a text file and returns formatted description."""
    with open(file_path) as file:
        lines = file.read().strip().splitlines()
    name = f"name: {lines[0]}"
    weight = f"weight: {lines[1]}"
    return f"{name}<br/>{weight}<br/><br/>"

def main():
    """Generate a PDF report from text files and send it via email."""
    # Set directory path for text files 
    TXT_DIR = "supplier-data/descriptions/"
    text_files = [os.path.join(TXT_DIR, file) for file in os.listdir(TXT_DIR) if file.endswith(".txt")]

    # Set report file path and name
    REPORT_FILE = "/tmp/processed.pdf"

    # Generate report body
    body = ""
    for file_path in text_files:
        body += get_description(file_path)

    # Set report title with today's date
    today = datetime.datetime.today()
    title = f"Processed Update on {today.strftime('%B')} {today.day}, {today.year}"

    # Generate PDF report
    reports.generate_report(REPORT_FILE, title, body)

    # Send email with report file
    data = {
        "sender": "automation@example.com",
        "receiver": f"{os.environ.get('USER')}@example.com",
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": REPORT_FILE,
    }
    message = emails.generate_email(**data)
    emails.send_email(message)

# Run main function
if __name__ == "__main__":
    main()
    