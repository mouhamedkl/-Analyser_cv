import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def analyze_cv(text):
    # Example analysis using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\+\d{3}\s\d{2}\s\d{3}\s\d{3}'
    skills_pattern = r'\b(?:Python|Java|C\+\+|JavaScript|Data Science|Machine Learning)\b'
    education_pattern = r'(?i)Formation\s*:\s*([^,]+)'
    project_pattern = r'(?i)project[s]?\s*:\s*([^,]+)'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    skills = re.findall(skills_pattern, text)
    education = re.findall(education_pattern, text)
    projects = re.findall(project_pattern, text)

    return emails, phones, skills, education, projects

if __name__ == "__main__":
    pdf_path = 'Cv.pdf'

    cv_text = extract_text_from_pdf(pdf_path)

    emails, phones, skills, education, projects = analyze_cv(cv_text)

    print("Emails:", emails)
    print("\n")
    print("Phone Numbers:", phones)
    print("\n")
    print("Skills:", skills)
    print("\n")
    print("Formation:", education)
    print("\n")
    print("Projects: \n", projects)
