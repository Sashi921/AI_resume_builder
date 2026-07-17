import os
import time

OUTPUT_FOLDER = "output/resumes"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def save_resume(resume):
    filename = f"resume_{int(time.time())}.txt"
    path = os.path.join(OUTPUT_FOLDER, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(resume)

    return filename