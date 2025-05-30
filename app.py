"""Import modules to obtain code data and set up Flask application
for code review."""
from flask import Flask, render_template_string
from ai_analysis import ai_prompt
from static_analysis import static_review

# Constant variables
AI_PROMPT_PATH = "ai_analysis/code_prompt.txt"
PYLINT_PROMPT_PATH = "static_analysis/pylint_prompt.txt"
INPUT_CODE_PATH = "inputcode.py"
STATIC_MODEL = "gpt-4.1-nano"
AI_MODEL = "gpt-4.1-mini"
STATIC_TEMP = 1
AI_TEMP = 0.2

# Initialize Flask application
app = Flask(__name__)

# Read prompts and input code
with open(AI_PROMPT_PATH, "r", encoding="utf-8") as file:
    review_prompt = file.read()

with open(PYLINT_PROMPT_PATH, "r", encoding="utf-8") as file:
    analysis_prompt = file.read()

with open(INPUT_CODE_PATH, "r", encoding="utf-8") as file:
    input_code = file.read()

# Add line numbers to input_code
INPUT_CODE = "\n".join(
    f"{idx}: {line}"
    for idx, line in enumerate(input_code.splitlines(), start=1)
)

# Generate AI and static analysis responses
static_code = static_review.run_pylint_on_file(INPUT_CODE_PATH)
static_response = ai_prompt.ai_prompt(
    static_code,
    analysis_prompt,
    STATIC_TEMP,
    STATIC_MODEL
)
html_response = ai_prompt.ai_prompt(INPUT_CODE, review_prompt, AI_TEMP,
                                    AI_MODEL)


@app.route('/')
def index():
    """Render the HTML inside a simple template"""
    return render_template_string(
        '<html><head><title>Code Review</title></head><body>'
        '<h1>AI Code Review Output</h1>{{ ai_content|safe }}'
        '<h1>Pylint Static Analysis Output</h1>{{ static_content|safe }}'
        '</body></html>',
        ai_content=html_response,
        static_content=static_response
    )


if __name__ == '__main__':
    app.run(debug=False)
