from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

class SkillMatcher:
    def __init__(self):
        self.job_profiles = [
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

    def match(self, candidate_skills):
        if not candidate_skills:
            return "No skills found", 0.0

        roles = []
        job_skills_texts = []

        for profile in self.job_profiles:
            roles.append(profile["role"])
            job_skills_texts.append(' '.join(profile["skills"]))

        resume_text = ' '.join(candidate_skills)
        corpus = [resume_text] + job_skills_texts

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(corpus)

        similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
        best_index = similarities.argmax()
        return roles[best_index], round(similarities[best_index], 2)