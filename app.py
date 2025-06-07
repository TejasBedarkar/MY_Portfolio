from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Premium Portfolio Data
ABOUT_ME = {
    'name': 'TEJAS BEDARKAR',
    'title': 'DATA & AI ENGINEER',
    'tagline': 'Transforming raw data into intelligent solutions',
    'description': 'Specialized in developing cutting-edge AI systems and data pipelines that drive business value. With expertise in machine learning, deep learning, and cloud technologies, I bridge the gap between data science and engineering.',
    'philosophy': 'Data first, insights second — that\'s my approach to solving complex problems',
    'education': 'B.E. in Artificial Intelligence and Data Science (CGPA: 8.21/10)',
    'contact': {
        'email': 'tejasbedarkar@gmail.com',
        'phone': '+91 8767719407',
        'location': 'Pune, Maharashtra, India'
    }
}

SERVICES = [
    {
        'title': 'AI/ML Engineering',
        'description': 'Design and deployment of production-grade machine learning systems',
        'icon': 'robot',
        'features': [
            'Custom model development',
            'Computer vision applications',
            'Natural language processing',
            'Predictive analytics'
        ]
    },
    {
        'title': 'Data Pipelines',
        'description': 'Building scalable ETL processes for enterprise data needs',
        'icon': 'database',
        'features': [
            'Data warehousing',
            'Real-time processing',
            'Data quality monitoring',
            'Workflow automation'
        ]
    },
    {
        'title': 'Cloud Solutions',
        'description': 'Architecting and implementing cloud-based data infrastructure',
        'icon': 'cloud',
        'features': [
            'AWS/GCP/Azure deployment',
            'Serverless architectures',
            'Container orchestration',
            'Cost optimization'
        ]
    }
]

PROJECTS = [
    {
        'title': 'Retinal Disease Diagnosis AI',
        'description': 'End-to-end deep learning system for detecting diabetic retinopathy and macular edema from retinal scans.',
        'tech': [
            {'name': 'Python', 'icon': 'python'},
            {'name': 'TensorFlow', 'icon': 'tensorflow'},
            {'name': 'OpenCV', 'icon': 'opencv'},
            {'name': 'Docker', 'icon': 'docker'}
        ],
        'github': 'https://github.com/TejasBedarkar/eye-disease-ai',
        'impact': [
            '95% diagnostic accuracy (vs. 87% human baseline)',
            '40% faster diagnosis process',
            'Deployed at 3 clinical centers'
        ],
        'image': 'retinal-ai.jpg'
    },
    {
        'title': 'Fraud Detection System',
        'description': 'Real-time machine learning pipeline for identifying fraudulent insurance claims.',
        'tech': [
            {'name': 'PySpark', 'icon': 'spark'},
            {'name': 'Scikit-learn', 'icon': 'sklearn'},
            {'name': 'AWS SageMaker', 'icon': 'aws'},
            {'name': 'FastAPI', 'icon': 'api'}
        ],
        'github': 'https://github.com/TejasBedarkar/fraud-detection',
        'impact': [
            '30% more fraud detected than manual review',
            '$2.8M annual savings for client',
            'Processing 5000+ claims/day'
        ],
        'image': 'fraud-detection.jpg'
    }
]

SKILLS = {
    'Languages': [
        {'name': 'Python', 'icon': 'python', 'level': 95},
        {'name': 'SQL', 'icon': 'database', 'level': 90},
        {'name': 'R', 'icon': 'r-project', 'level': 80}
    ],
    'Data Science': [
        {'name': 'Pandas', 'icon': 'pandas', 'level': 90},
        {'name': 'NumPy', 'icon': 'numpy', 'level': 85},
        {'name': 'SciPy', 'icon': 'scipy', 'level': 80}
    ],
    'Machine Learning': [
        {'name': 'TensorFlow', 'icon': 'tensorflow', 'level': 85},
        {'name': 'PyTorch', 'icon': 'pytorch', 'level': 80},
        {'name': 'Scikit-learn', 'icon': 'sklearn', 'level': 90}
    ],
    'DevOps & Cloud': [
        {'name': 'Docker', 'icon': 'docker', 'level': 85},
        {'name': 'AWS', 'icon': 'aws', 'level': 80},
        {'name': 'Kubernetes', 'icon': 'kubernetes', 'level': 75}
    ]
}

TESTIMONIALS = [
    {
        'quote': 'Tejas transformed our data analysis process with his innovative AI solutions that delivered measurable business impact.',
        'author': 'CTO, Saavi Softwares',
        'position': 'Chief Technology Officer'
    },
    {
        'quote': 'The fraud detection system developed by Tejas saved us millions in fraudulent claims while maintaining excellent precision.',
        'author': 'Director of Analytics',
        'position': 'Fortune 500 Insurance Company'
    }
]

@app.route('/')
def home():
    return render_template('home.html', 
                         about=ABOUT_ME, 
                         services=SERVICES,
                         testimonials=TESTIMONIALS)

@app.route('/about')
def about():
    return render_template('about.html', 
                         about=ABOUT_ME, 
                         skills=SKILLS)

@app.route('/services')
def services():
    return render_template('services.html', 
                         services=SERVICES,
                         about=ABOUT_ME)

@app.route('/projects')
def projects():
    return render_template('projects.html', 
                         projects=PROJECTS,
                         about=ABOUT_ME)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here you would typically process the form data
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', 
                         contact=ABOUT_ME['contact'],
                         about=ABOUT_ME)

if __name__ == '__main__':
    app.run(debug=True)