import os
import re

def create_course_content():
    base_dir = "/Users/rakesh/Desktop/Workspace/PythonProject/30-Days-Python-SDET-Challenge"
    readme_path = os.path.join(base_dir, "README.md")
    
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Find the table rows for Day 05 to Day 30
    pattern = r"\| (Day \d{2}) \| (.*?) \| (.*?) \|"
    matches = re.findall(pattern, readme_content)
    
    new_readme_content = readme_content
    
    for match in matches:
        day_str = match[0] # e.g., "Day 05"
        topic = match[1].strip() # e.g., "Conditional Statements"
        status = match[2].strip()
        
        # We only process if it's Day 05 or later and it doesn't have a link yet
        if not ("[" in topic and "]" in topic):
            day_num = int(day_str.split()[1])
            if day_num >= 5:
                # Format the folder name
                # Remove special characters, replace spaces with hyphens
                clean_topic = re.sub(r'[^a-zA-Z0-9\s-]', '', topic)
                folder_suffix = clean_topic.strip().replace(" ", "-")
                folder_name = f"Day-{day_num:02d}-{folder_suffix}"
                
                day_path = os.path.join(base_dir, folder_name)
                
                # Create directory
                os.makedirs(day_path, exist_ok=True)
                
                # Create files
                with open(os.path.join(day_path, "README.md"), "w", encoding="utf-8") as f:
                    f.write(f"# 📚 {day_str}: {topic}\n\n## Overview\n\nIntroduction to {topic}.\n\n## Key Concepts\n- Concept 1\n- Concept 2\n\n## References\n- [Official Documentation](https://docs.python.org/3/)\n")
                
                with open(os.path.join(day_path, "Python_Notes.md"), "w", encoding="utf-8") as f:
                    f.write(f"# 📝 {day_str} Notes: {topic}\n\n## Detailed Explanation\n\nWrite detailed notes here...\n\n```python\n# Code examples go here\n```\n")
                
                with open(os.path.join(day_path, "practice_questions.md"), "w", encoding="utf-8") as f:
                    f.write(f"# 💻 {day_str} Practice Questions: {topic}\n\n### Easy\n1. Question 1...\n\n### Medium\n1. Question 1...\n\n### Hard\n1. Question 1...\n")
                
                with open(os.path.join(day_path, "examples.py"), "w", encoding="utf-8") as f:
                    f.write(f'# {day_str} Examples: {topic}\n\ndef example_function():\n    pass\n\nif __name__ == "__main__":\n    print("{topic} examples run.")\n')
                
                with open(os.path.join(day_path, "assignments.py"), "w", encoding="utf-8") as f:
                    f.write(f'# {day_str} Assignments: {topic}\n\n# TODO: Complete assignments here\n')
                    
                # Update main README.md
                old_row = f"| {day_str} | {topic} | {status} |"
                new_row = f"| {day_str} | [{topic}](./{folder_name}) | ✅ Completed |"
                new_readme_content = new_readme_content.replace(old_row, new_row)
                
                print(f"Generated {folder_name}")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme_content)
        
    print("Main README.md updated.")

if __name__ == "__main__":
    create_course_content()
