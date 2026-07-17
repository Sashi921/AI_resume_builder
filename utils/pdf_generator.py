import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER

def generate_pdf(filename):

    txt_path = os.path.join("output/resumes", filename)

    pdf_name = filename.replace(".txt", ".pdf")
    pdf_path = os.path.join("output/resumes", pdf_name)

    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read()

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    lines = content.split("\n")

    first = True

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1,8))
            continue

        if first:
            story.append(Paragraph(line, title))
            story.append(Spacer(1,12))
            first = False
            continue

        if line.isupper():
            story.append(Spacer(1,10))
            story.append(Paragraph(line, heading))
            story.append(Spacer(1,5))
        else:
            story.append(Paragraph(line, normal))

    doc.build(story)

    return pdf_path