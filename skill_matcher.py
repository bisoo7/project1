from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 

class skillMatcher:
    def __init__(self):  # Dictionary of job profiles
        self.jobProfiles = [
            {
                "role": "Data Scientist",
                "skills": ["python", "machine learning", "data analysis", "numpy", "pandas"]
            },
            {
                "role": "Web Developer",
                "skills": ["html", "css", "javascript", "react", "flask"]
            },
            {
                "role": "Mobile Developer",
                "skills": ["java", "kotlin", "android", "flutter", "dart"]
            },
            {
                "role": "Business Analyst",
                "skills": ["excel", "sql", "data analysis", "power bi", "communication"]
            }
        ]

    def match(self, employeeSkills):
        if not employeeSkills:
            return "No skills found", 0.0

        roles = []
        jobSkills = []

        for profile in self.jobProfiles:  # Assigning skills to roles
            roles.append(profile["role"]) 
            jobSkills.append(' '.join(profile["skills"]))

        resumeText = ' '.join(employeeSkills)  # Joining skills with space
        corpus = [resumeText] + jobSkills  # Combining candidate's skills with required skills for the role

        vectorizer = TfidfVectorizer()  
        vectors = vectorizer.fit_transform(corpus)  # Using TF-IDF method to evaluate the importance of a skill in the resume relative to the collection of skills in the roles' required skill set

        similarities = cosine_similarity(vectors[0], vectors[1:]).flatten()  # Using cosine similarity to calculate the distance between skills based on their feature dimensions in a dataset. A smaller distance indicates higher similarity
        bestJobIndex = similarities.argmax()
        return roles[bestJobIndex], round(similarities[bestJobIndex], 2)  # Returns the most relevant role and the percentage of how compatible the candidate is for the job
