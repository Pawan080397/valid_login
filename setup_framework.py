import os

# Folder structure dict
folders = [
    "tests/login",
    "tests/dashboard",
    "tests/api",
    "pages",
    "utilities",
    "configs",
    "reports/screenshots",
    "reports/html_reports",
    "jenkins"
]

# Files to auto-create with optional default content
files = {
    "requirements.txt": """selenium
pytest
webdriver-manager
pytest-html
pyyaml
requests""",

    "README.md": "# Selenium Automation Framework (Python + Pytest + Jenkins)\n",

    "configs/config.yaml": """base_url: "https://example.com"
username: "admin"
password: "password123"
""",

    "jenkins/Jenkinsfile": """pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Run Tests') {
            steps { sh 'pytest --html=reports/html_reports/report.html --self-contained-html' }
        }
        stage('Archive Reports') {
            steps { archiveArtifacts artifacts: 'reports/html_reports/*.html', fingerprint: true }
        }
    }
}""",

    "tests/login/test_login_valid.py": """def test_login_valid():
    assert True
""",

    "tests/login/test_login_invalid.py": """def test_login_invalid():
    assert True
""",

    "pages/login_page.py": """class LoginPage:
    def __init__(self, driver):
        self.driver = driver
""",

    "utilities/webdriver_setup.py": """from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    return driver
""",

    ".gitignore": """__pycache__/
*.pyc
reports/html_reports/
reports/screenshots/
.env
.vscode/
"""
}


def create_structure():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"[Created] {folder}")

    # Create files
    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[Created] {file_path}")

    print("\n🎉 Framework Setup Complete! Now you can start adding your test cases.\n")


if __name__ == "__main__":
    create_structure()
