from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PDF_FOLDER'] = 'static/pdfs'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PDF_FOLDER'], exist_ok=True)

# دیتا جزئیات پروژه‌ها
projects = {
    "FRP": {
        "title": "FRP Project",
        "status": "In Progress",
        "progress": 70,
        "estimated_completion": "15 June 2025"
    },
    "Nano": {
        "title": "Nano Research",
        "status": "In Progress",
        "progress": 50,
        "estimated_completion": "10 July 2025"
    },
    "CPT": {
        "title": "CPT-CNN-LSTM-GNN",
        "status": "In Progress",
        "progress": 50,
        "estimated_completion": "25 July 2025"
    }
}

courses = {
    "CS1": {
        "title": "Concrete Structures 1",
        "instructor": "Vahab Toufigh, Ph.D., P.E.",
        "TA": "Mohammad Shamsi",
        "sessions": [
            {
                "title": "Session 1 - Materials",
                "materials": [
                    {"title": "Part 1", "filename": "Part1_Material_stu.pdf"}
                ]
            },
            {
                "title": "Session 2 - Flexural Design",
                "materials": [
                    {"title": "Part 1", "filename": "Part2_1_ED_Flexure_stu.pdf"},
                    {"title": "Part 2", "filename": "Part2_2_SDM.pdf"},
                    {"title": "Part 3", "filename": "Part2_3_SDM.pdf"}
                ]
            },
            {
                "title": "Session 3 - Shear",
                "materials": [
                    {"title": "Part 1", "filename": "Part3_1_Shear_stu.pdf"},
                    {"title": "Part 2", "filename": "Part3_2_Shear_stu.pdf"}
                ]
            },
            {
                "title": "Session 4 - Torsion",
                "materials": [
                    {"title": "Part 1", "filename": "Part4_Torsion_stu.pdf"}
                ]
            },
            {
                "title": "Session 5 - Short Columns",
                "materials": [
                    {"title": "Part 1", "filename": "Part5_1_Short_column.pdf"},
                    {"title": "Part 2", "filename": "Part5_2_Short_column.pdf"}
                ]
            },
            {
                "title": "Session 6 - Development length",
                "materials": [
                    {"title": "Part 1", "filename": "Part6_1_development_length.pdf"},
                    {"title": "Part 2", "filename": "Part6_2_development_length.pdf"}
                ]
            },
            {
                "title": "Session 7 - Serviceability",
                "materials": [
                    {"title": "Part 1", "filename": "Part7-1-Serviceability.pdf"},
                    {"title": "Part 2", "filename": "Part7-2-Serviceability.pdf"}
                ]
            },
            {
                "title": "Session 8 - One-Way Slabs",
                "materials": [
                    {"title": "Part 1", "filename": "Part8-1-Oneway-Slab.pdf"},
                    {"title": "Part 2", "filename": "Part8-2-Oneway-Slab.pdf"}
                ]
            },
            {
                "title": "Session 9 - Slender Columns",
                "materials": [
                    {"title": "Part 1", "filename": "Part9-1-Slender-columns.pdf"},
                    {"title": "Part 2", "filename": "Part9-2-Slender-columns.pdf"}
                ]
            }
        ],
        "resources": [
            {"title": "David Darwin, Charles W.Dolan. Design of concrete structures. 16th", "filename": "Design_of_Concrete_Structures,_by_David_Darwin.pdf"}
        ]
    },


    "CS2": {
        "title": "Concrete Structures 2",
        "instructor": "Vahab Toufigh, Ph.D., P.E.",
        "TA": "Mohammad Shamsi",
        "sessions": [
            {
                "title": "Session 1 - Two-Way Slabs",
                "materials": [
                    
                ]
            },
            {
                "title": "Session 2 - Foundation",
                "materials": [
                    
                ]
            },
            {
                "title": "Session 3 - Shear wall",
                "materials": [
                    
                ]
            },
            {
                "title": "Session 4 - Retaining wall",
                "materials": [
                    
                ]
            },
            {
                "title": "Session 5 - Conections",
                "materials": [
                    
                ]
            }
        ],
        "resources": [
            {"title": "David Darwin, Charles W.Dolan. Design of concrete structures. 16th", "filename": "Design_of_Concrete_Structures,_by_David_Darwin.pdf"}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', projects=projects, courses=courses)

@app.route('/project/<project_name>')
def project_details(project_name):
    project = projects.get(project_name)
    if not project:
        return "Project not found", 404
    return render_template('project_details.html', project=project)

@app.route('/download/<filename>')
def download_pdf(filename):
    return send_from_directory(app.config['PDF_FOLDER'], filename)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/upload/<project_name>', methods=['POST'])
def upload_file(project_name):
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = f"{project_name}_{file.filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('project_details', project_name=project_name))

@app.route('/course/<course_name>')
def course_details(course_name):
    course = courses.get(course_name)
    if not course:
        return "Course not found", 404
    return render_template('course_details.html', course=course)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)