# Day 01: Python Setup & Environment

## 📌 Topic Introduction
Welcome to Day 1! Before writing any automation scripts, we need to set up a robust foundation. Today is all about installing Python, configuring an Integrated Development Environment (IDE) like PyCharm or VS Code, and running our very first Python script. 

## 📖 Theory
### What is Python?
Python is a high-level, interpreted programming language known for its readability and simplicity. 

### Why this topic matters in QA
As an SDET or QA Automation Engineer, you will not just run scripts; you will maintain frameworks, install dependencies, and run tests on different environments (Windows, macOS, Linux, CI/CD pipelines). Understanding how Python is installed, how paths work, and how an IDE executes code is critical for troubleshooting "works on my machine" issues.

### Real-world examples
- **Environment Setup:** Setting up a Jenkins or GitHub Actions agent to run your tests requires installing the correct version of Python and dependencies. 
- **IDE debugging:** Debugging a flaky test using VS Code breakpoints instead of relying on `print()` statements.

## 🌟 Best Practices
- **Never use the system Python on macOS/Linux:** Always install a separate Python version for development (using `pyenv` or official installers) to avoid corrupting OS-level tools.
- **Use an IDE, not a text editor:** Tools like PyCharm Community or VS Code provide syntax highlighting, autocompletion, and debugging—essential for automation frameworks.
- **Add Python to PATH:** Always ensure the `python` or `python3` executable is in your system's environment variables.

## ⚠️ Common Mistakes
- Installing multiple Python versions and running the wrong one (e.g., typing `python script.py` when it defaults to Python 2.7 instead of 3.x).
- Forgetting to check the "Add Python to PATH" box during installation on Windows.
- Writing code in a plain text file without `.py` extension.

## 🗣️ Interview Questions
1. **What is the difference between interpreted and compiled languages? Why is Python called interpreted?**
   *Answer:* Compiled languages (like Java/C++) translate code into machine code before running. Interpreted languages (like Python) read and execute code line-by-line via an interpreter.
2. **How do you check which version of Python is running in your terminal?**
   *Answer:* By running `python --version` or `python3 --version`.
3. **What is PATH in operating systems, and why does Python need to be added to it?**
   *Answer:* PATH is an environment variable specifying directories where executable programs are located. Adding Python to PATH allows you to run `python` commands from any directory in the terminal.

## 📝 Summary
Today we laid the groundwork. We learned how to install Python, configure an IDE, and write a simple script. This is the first step towards writing complex automation frameworks!
