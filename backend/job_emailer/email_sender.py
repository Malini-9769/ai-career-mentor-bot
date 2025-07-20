import os
import smtplib
from email.mime.text import MIMEText

def send_job_email(recipient_email, job_list):
    body = ""
    for job in job_list:
        body += f"📄 {job['file']}\n✅ Matched Skills: {', '.join(job['matched_skills'])}\n❌ Missing Skills: {', '.join(job['missing_skills'])}\n📊 Fit Score: {job['fit_score']}\n\n"

    msg = MIMEText(body)
    msg['Subject'] = 'Your Weekly Job Matches'
    msg['From'] = os.environ['EMAIL_USER']
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL(os.environ['EMAIL_HOST'], int(os.environ['EMAIL_PORT'])) as server:
        server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
        server.send_message(msg)

    print(f"✅ Email sent to {recipient_email}")




# import smtplib
# from email.mime.text import MIMEText

# def send_job_email(recipient_email, job_list):
#     body = ""
#     for job in job_list:
#         body += f"📄 {job['file']}\n✅ Matched Skills: {', '.join(job['matched_skills'])}\n❌ Missing Skills: {', '.join(job['missing_skills'])}\n📊 Fit Score: {job['fit_score']}\n\n"

#     msg = MIMEText(body)
#     msg['Subject'] = 'Your Weekly Job Matches'
#     msg['From'] = os.environ['EMAIL_USER']
#     msg['To'] = recipient_email

#     with smtplib.SMTP_SSL(os.environ['EMAIL_HOST'], int(os.environ['EMAIL_PORT'])) as server:
#         server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
#         server.send_message(msg)

#     print(f"✅ Email sent to {recipient_email}")
