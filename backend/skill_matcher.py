def match_skills(user_skills, job_list):
    matched_jobs = []
    
    for job in job_list:
        job_skills = job.get("skills", [])
        matched = list(set(user_skills) & set(job_skills))
        missing = list(set(job_skills) - set(user_skills))

        if job_skills:
            fit_score = round(len(matched) / len(job_skills), 2)
        else:
            fit_score = 0.0

        matched_jobs.append({
            "file": job.get("file", "unknown"),
            "matched_skills": matched,
            "missing_skills": missing,
            "fit_score": fit_score
        })

    return matched_jobs


# def match_skills(user_skills, jd_text):
#     return {'fit_score': 80, 'missing_skills': []}
