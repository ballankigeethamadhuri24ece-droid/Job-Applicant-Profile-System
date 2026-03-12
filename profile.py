class PersonalInfo:
    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def display_personal_info(self):
        print(f"Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Contact: {self.contact}")
        print(f"Email: {self.email}")

class Education(PersonalInfo):
    def __init__(self, name, dob, contact, email, degree, university, graduation_year, cgpa):
        super().__init__(name, dob, contact, email)
        self.degree = degree
        self.university = university
        self.graduation_year = graduation_year
        self.cgpa = cgpa

    def display_education(self):
        print(f"Degree: {self.degree}")
        print(f"University: {self.university}")
        print(f"Year of Graduation: {self.graduation_year}")
        print(f"CGPA: {self.cgpa}")

class Experience(Education):
    def __init__(self, name, dob, contact, email, degree, university, graduation_year, cgpa,
                 company, job_role, years_exp, skills):
        super().__init__(name, dob, contact, email, degree, university, graduation_year, cgpa)
        self.company = company
        self.job_role = job_role
        self.years_exp = years_exp
        self.skills = skills

    def display_experience(self):
        print(f"Company: {self.company}")
        print(f"Job Role: {self.job_role}")
        print(f"Years of Experience: {self.years_exp}")
        print(f"Skills: {', '.join(self.skills)}")

class CandidateProfile(Experience):
    def __init__(self, name, dob, contact, email, degree, university, graduation_year, cgpa,
                 company, job_role, years_exp, skills):
        super().__init__(name, dob, contact, email, degree, university, graduation_year, cgpa,
                         company, job_role, years_exp, skills)

    def display_complete_profile(self):
        print("="*40)
        self.display_personal_info()
        self.display_education()
        self.display_experience()
        print(f"Eligibility: {self.check_eligibility()}")
        print("="*40)

    def check_eligibility(self):
        if self.years_exp > 5:
            return "Eligible for Senior Role"
        else:
            return "Eligible for Junior Role"


# Example usage for 2 candidates
candidate1 = CandidateProfile(
    "Geetha", "1995-06-15", "9876543210", "geetha@example.com",
    "B.Tech", "ANITS", 2017, 8.5,
    "TechCorp", "Software Engineer", 6, ["Python", "Java", "SQL"]
)

candidate2 = CandidateProfile(
    "Surya", "1996-11-10", "9123456780", "surya@example.com",
    "B.Tech", "ANITS", 2018, 8.2,
    "SoftSolutions", "Junior Developer", 4, ["C++", "Python", "HTML"]
)

candidate1.display_complete_profile()
candidate2.display_complete_profile()