import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

client = Groq(api_key=API_KEY)


def generate_resume(data):

    education = ""
    for edu in data["education"]:
        education += f"""
Degree : {edu['degree']}
College : {edu['college']}
Year : {edu['year']}
"""

    experience = ""
    for exp in data["experience"]:
        experience += f"""
Role : {exp['role']}
Company : {exp['company']}
Duration : {exp['duration']}
Description : {exp['description']}
"""

    projects = ""
    for pro in data["projects"]:
        projects += f"""
Project Title : {pro['title']}
Project Description : {pro['description']}
"""

    prompt = f"""
You are an expert ATS Resume Writer.

Create a professional one-page resume.

IMPORTANT RULES

- Return ONLY the resume.
- No notes.
- No markdown.
- No explanation.
- Use professional language.
- Use headings.
- Use bullet points.
- Keep formatting clean.

Candidate Details

Name : {data['name']}
Email : {data['email']}
Phone : {data['phone']}
Location : {data['location']}

Professional Summary

{data['summary']}

Skills

{", ".join(data["skills"])}

Education

{education}

Experience

{experience}

Projects

{projects}

Generate exactly like this.

================================================

{data['name'].upper()}

{data['email']} | {data['phone']} | {data['location']}

PROFESSIONAL SUMMARY

Write a strong professional summary.

------------------------------------------------

SKILLS

• Skill 1

• Skill 2

• Skill 3

------------------------------------------------

EDUCATION

Degree : B.Tech Computer Science

College : ABC Engineering College

Year : 2026

------------------------------------------------

PROFESSIONAL EXPERIENCE

Role : Python Developer

Company : Infosys

Duration : Jan 2024 - Present

Responsibilities

• Point 1

• Point 2

• Point 3

------------------------------------------------

PROJECTS

Project Title : AI Resume Builder

Description

• Developed using Flask

• Integrated Groq API

• Generated PDF Resume

================================================

Replace the example values with the candidate details provided.

Return only the resume.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a professional ATS resume writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1800
    )

    return response.choices[0].message.content