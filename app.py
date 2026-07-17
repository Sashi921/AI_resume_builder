from flask import Flask, render_template, request, send_file
import os

from utils.ai_helper import generate_resume
from utils.helpers import validate_input
from utils.file_handler import save_resume
from utils.pdf_generator import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "assets/data"
OUTPUT_FOLDER = "output/resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "location": request.form.get("location"),
            "summary": request.form.get("summary"),
            "skills": request.form.get("skills", "").split(","),

            "education": [{
                "degree": request.form.get("degree"),
                "college": request.form.get("college"),
                "year": request.form.get("year")
            }],

            "experience": [{
                "company": request.form.get("company"),
                "role": request.form.get("role"),
                "duration": request.form.get("duration"),
                "description": request.form.get("description")
            }],

            "projects": [{
                "title": request.form.get("project"),
                "description": request.form.get("project_description")
            }]
        }

        if not validate_input(data):
            return "Invalid Input"

        resume = generate_resume(data)

        filename = save_resume(resume)

        return render_template(
            "preview.html",
            resume=resume,
            filename=filename
        )

    except Exception as e:
        return f"Error: {e}"


@app.route("/download/<filename>")
def download(filename):
    pdf_path = generate_pdf(filename)
    return send_file(pdf_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)