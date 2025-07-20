# def fetch_jobs(query='data scientist'):
#     return [{'title': 'DS', 'company': 'X', 'url': '#', 'tags': ['python']}]

import os

# Optional: define a basic list of common tech skills to search for
COMMON_SKILLS = [
    "python", "machine learning", "deep learning", "tensorflow", "keras", "pytorch",
    "nlp", "data analysis", "sql", "excel", "power bi", "aws", "gcp", "azure",
    "docker", "kubernetes", "flask", "django", "javascript", "git"
]

def extract_skills_from_text(text):
    found = [skill for skill in COMMON_SKILLS if skill in text.lower()]
    return found

def fetch_jobs(folder_path):
    jobs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = f.read()
                skills = extract_skills_from_text(content)
                jobs.append({
                    "file": filename,
                    "skills": skills
                })
    return jobs
