# def run_scheduler():
#     print('Scheduler running')

import os
from job_fetcher import fetch_jobs
# from skill_matcher import match_skills
from email_sender import get_user_profile

# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# output_dir = "job_matches"
# os.makedirs(output_dir, exist_ok=True)

# Add absolute path to backend directory
skill_matcher_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, skill_matcher_path)

from skill_matcher import match_skills


user = get_user_profile()
jobs = fetch_jobs()
matched_jobs = match_skills(user['skills'], jobs)

output_path = os.path.join(output_dir, "weekly_matches.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"Weekly Matches for {user['name']} ({user['email']}):\n\n")
    for job in matched_jobs:
        f.write(f"- {job['title']}: {job['description'][:150]}...\n\n")

print(f"✅ Job matches saved to: {output_path}")
