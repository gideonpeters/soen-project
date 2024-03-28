class JobMarketplace:
    def __init__(self):
        self.job_listings = []
        self.resumes = []

    def post_job(self, job_title, company, requirements):
        self.job_listings.append({'job_title': job_title, 'company': company, 'requirements': requirements})

    def remove_job(self, job):
        self.job_listings.remove(job)

    def submit_resume(self, name, skills, experience):
        self.resumes.append({'name': name, 'skills': skills, 'experience': experience})

    def withdraw_resume(self, resume):
        self.resumes.remove(resume)

    def search_jobs(self, skill):
        return [job for job in self.job_listings if skill in job['requirements']]

    def get_job_applicants(self, job):
        return [resume for resume in self.resumes if all(skill in resume['skills'] for skill in job['requirements'])]

    def matches_requirements(self, resume, requirements):
        return all(skill in resume['skills'] for skill in requirements)
