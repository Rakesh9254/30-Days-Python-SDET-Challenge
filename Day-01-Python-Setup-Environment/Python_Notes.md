# Python Notes: Setup and Environment

## 1. Installing Python
1. Go to [python.org](https://www.python.org/downloads/).
2. Download the latest version for your OS.
3. **Windows users:** MUST check the box "Add python.exe to PATH" at the bottom of the installer.
4. **macOS users:** Python 3 is often installed by default, or you can use `brew install python`.

### Verification
Open terminal/command prompt and type:
```bash
python --version
# OR
python3 --version
```
Expected output: `Python 3.10.x` (or newer)

## 2. Setting up the IDE (VS Code)
We recommend **Visual Studio Code (VS Code)** for its excellent extensions and lightweight nature.

1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Open VS Code.
3. Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X).
4. Search for "Python" (by Microsoft) and install it.

## 3. Writing Your First Script
1. Create a folder named `Automation_Project`.
2. Open that folder in VS Code (`File > Open Folder`).
3. Create a new file named `hello_world.py`.
4. Write the following code:
```python
print("Hello, SDET World!")
```

## 4. Running the Script
### From IDE
- In VS Code, click the **Play (Run)** button in the top right corner.

### From Terminal (Crucial for CI/CD)
1. Open the terminal.
2. Navigate to your folder (`cd Automation_Project`).
3. Run:
```bash
python hello_world.py
# OR
python3 hello_world.py
```

## 5. QA Perspective: Why do we care?
In QA automation, you rarely run tests by clicking a button in an IDE. You run them from the command line so they can be integrated into CI/CD pipelines (Jenkins, GitLab, GitHub Actions). Knowing how to navigate directories in the terminal and execute Python files is a fundamental SDET skill.
