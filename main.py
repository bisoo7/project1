from resume_reader import ResumeReader
from skill_matcher import SkillMatcher

def main():
    file_path = input("Enter the path to the resume (PDF or DOCX): ")

    try:
        reader = ResumeReader(file_path)
        reader.extract_text()

        name = reader.extract_name()
        email = reader.extract_email()
        skills = reader.extract_skills()

        print("\n--- Resume Summary ---")
        print(f"Name: {name}")
        print(f"Email: {email if email else 'Not found'}")
        print(f"Skills: {', '.join(skills) if skills else 'None found'}")

        matcher = SkillMatcher()
        role, score = matcher.match(skills)

        print(f"\nBest Matched Job Role: {role} (Match Score: {int(100*score)}%)")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()