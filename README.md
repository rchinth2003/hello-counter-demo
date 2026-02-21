# HelloCounter API

Minimal FastAPI-based demo with two endpoints: `/hello` and `/counter`.

Run locally:

```bash
python -m pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

Run tests:

```bash
pytest -q
```
# Python virtual environment setup

Python was not found on PATH when attempting to create a virtual environment from the workspace.

Once Python is installed or available on PATH, create the virtual environment from the project root:

PowerShell (recommended on Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Command Prompt (cmd.exe):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

Git Bash / macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Verify the environment Python version (Windows):

```powershell
.\.venv\Scripts\python.exe -V
```

If you don't have Python installed, download it from: https://www.python.org/downloads/
