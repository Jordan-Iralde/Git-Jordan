import os

def create_project_structure(structure):
    for path in structure:
        if path.endswith('/'):
            os.makedirs(path, exist_ok=True)  # Crear directorio
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)  # Asegura que el directorio padre exista
            with open(path, 'w') as f:
                pass  # Crear archivo

project_structure = [
    "voice_cloning_project/",
    "voice_cloning_project/data/",
    "voice_cloning_project/data/raw/",
    "voice_cloning_project/data/processed/",
    "voice_cloning_project/models/",
    "voice_cloning_project/models/checkpoints/",
    "voice_cloning_project/models/pretrained/",
    "voice_cloning_project/scripts/",
    "voice_cloning_project/scripts/preprocess.py",
    "voice_cloning_project/scripts/train.py",
    "voice_cloning_project/scripts/synthesize.py",
    "voice_cloning_project/web_app/",
    "voice_cloning_project/web_app/app.py",
    "voice_cloning_project/web_app/templates/",
    "voice_cloning_project/web_app/templates/index.html",
    "voice_cloning_project/requirements.txt",
    "voice_cloning_project/README.md"
]

if __name__ == "__main__":
    create_project_structure(project_structure)


'''
Sacado de aca de esta manera

voice_cloning_project/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   ├── checkpoints/
│   └── pretrained/
├── scripts/
│   ├── preprocess.py
│   ├── train.py
│   └── synthesize.py
├── web_app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── requirements.txt
└── README.md
'''