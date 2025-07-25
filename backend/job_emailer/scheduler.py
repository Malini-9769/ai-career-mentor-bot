import sys
import os

# Set base directory to project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, os.path.join(BASE_DIR, "backend"))

from skill_matcher import match_skills
from job_fetcher import fetch_jobs

# Define user skills
skills = ["Python", "Machine Learning", "NLP"]

# Load job descriptions
job_folder = os.path.join(BASE_DIR, "data", "job_descriptions")
job_matches = match_skills(skills, fetch_jobs(job_folder))

# Output directory for the file
output_dir = os.path.join(BASE_DIR, "job_matches")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "weekly_matches.txt")

# Save job matches with detailed info
with open(output_path, "w", encoding="utf-8") as f:
    for job in job_matches:
        if isinstance(job, dict):
            file_name = job.get("file", "Unknown File")
            matched = ", ".join(job.get("matched_skills", []))
            missing = ", ".join(job.get("missing_skills", []))
            fit_score = job.get("fit_score", "N/A")
            f.write(
                f"📄 {file_name}\n"
                f"✅ Matched Skills: {matched}\n"
                f"❌ Missing Skills: {missing}\n"
                f"📊 Fit Score: {fit_score}\n\n"
            )
        else:
            f.write(f"{job}\n\n")

print(f"✅ Job matches with fit scores saved to: {output_path}")

from email_sender import send_job_email

# import os

recipient = os.getenv("RECIPIENT_EMAIL")
if recipient:
    send_job_email(recipient, job_matches)
else:
    print("⚠️ No RECIPIENT_EMAIL found in environment variables.")











# # # def run_scheduler():
# # #     print('Scheduler running')

# # import os
# # from job_fetcher import fetch_jobs
# # # from skill_matcher import match_skills
# # from email_sender import get_user_profile

# # # import sys
# # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # # output_dir = "job_matches"
# # # os.makedirs(output_dir, exist_ok=True)

# # # Add absolute path to backend directory
# # skill_matcher_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # sys.path.insert(0, skill_matcher_path)

# # from skill_matcher import match_skills


# # user = get_user_profile()
# # jobs = fetch_jobs()
# # matched_jobs = match_skills(user['skills'], jobs)

# # output_path = os.path.join(output_dir, "weekly_matches.txt")
# # with open(output_path, "w", encoding="utf-8") as f:
# #     f.write(f"Weekly Matches for {user['name']} ({user['email']}):\n\n")
# #     for job in matched_jobs:
# #         f.write(f"- {job['title']}: {job['description'][:150]}...\n\n")

# # print(f"✅ Job matches saved to: {output_path}")



# import sys
# import os

# # Add backend/ to the import path
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.insert(0, BASE_DIR)

# from skill_matcher import match_skills
# from job_fetcher import fetch_jobs

# # Hardcoded skill list (or later load from a config file)
# skills = ["Python", "Machine Learning", "NLP"]

# # Fetch jobs from your job_descriptions/ folder
# job_folder = os.path.join(BASE_DIR, "../data/job_descriptions")
# job_matches = match_skills(skills, fetch_jobs(job_folder))

# # Ensure output folder exists
# output_dir = os.path.join(BASE_DIR, "../../job_matches")
# os.makedirs(output_dir, exist_ok=True)

# output_path = os.path.join(output_dir, "weekly_matches.txt")

# # Save results
# with open(output_path, "w", encoding="utf-8") as f:
#     for job in job_matches:
#         if isinstance(job, dict) and "file" in job and "matched_skills" in job:
#             f.write(f"{job['file']}\nMatched Skills: {', '.join(job['matched_skills'])}\n\n")
#         else:
#             f.write(f"{job}\n\n")  # fallback if job is not in expected format
#         # f.write(f"{job['file']}\nMatched Skills: {', '.join(job['matched_skills'])}\n\n")

# print(f"✅ Job matches saved to: {output_path}")


# import sys
# import os

# # Set base directory to project root
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
# sys.path.insert(0, os.path.join(BASE_DIR, "backend"))

# from skill_matcher import match_skills
# from job_fetcher import fetch_jobs

# # Define skills manually or from config
# skills = ["Python", "Machine Learning", "NLP"]

# # Path to job descriptions
# job_folder = os.path.join(BASE_DIR, "data", "job_descriptions")

# # Fetch and match jobs
# job_matches = match_skills(skills, fetch_jobs(job_folder))

# # Output path
# output_dir = os.path.join(BASE_DIR, "job_matches")
# os.makedirs(output_dir, exist_ok=True)
# output_path = os.path.join(output_dir, "weekly_matches.txt")

# # Debug info
# print(f"🔍 Writing results to: {output_path}")
# print(f"📄 Total matches found: {len(job_matches)}")

# # Write job matches to file
# with open(output_path, "w", encoding="utf-8") as f:
#     for job in job_matches:
#         if isinstance(job, dict) and "file" in job and "matched_skills" in job:
#             f.write(f"{job['file']}\nMatched Skills: {', '.join(job['matched_skills'])}\n\n")
#         else:
#             f.write(f"{job}\n\n")  # fallback for unexpected formats

# print("✅ Job matches saved successfully!")

