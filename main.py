from resume_reader import resumeReader
from skill_matcher import skillMatcher

def main():
    file_path = r"C:\Users\Abdullah\OneDrive - University of Jeddah\Second year\Second Sim\python programming course\Project\resume_analyzer_project\examples\sample_resume_5.docx"
    
    try: 
        reader = resumeReader(file_path)  # Using method from resume_reader file, reads files of type pdf/docx
        reader.extractText()  # Extract the text as plain text from the document

        name = reader.extractName()  # Extracting name into text using resume_reader class
        email = reader.extractEmail()  # Extracting email into text using resume_reader class
        skills = reader.extractSkills()  # Extracting skills into text using resume_reader class

        # Displaying the result
        print("\n--- Resume Summary ---")
        print(f"Name: {name}")
        print(f"Email: {email if email else 'Not found'}")
        print(f"Skills: {', '.join(skills) if skills else 'None found'}")

        matcher = skillMatcher()  # Using method from skill_matcher file, compares skills to reach most suitable job
        role, score = matcher.match(skills)  # matcher has two returns, Role{string} and Score{float}

        print(f"\nBest Matched Job Role: {role} (Match Score: {int(100*score)}%)")

    except Exception as e:  # Catching any error that could occur
        print(f"\nError: {str(e)}")

if __name__ == "__main__":  # Main function to provide better readability
    main()
