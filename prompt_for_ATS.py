def prompt(resume_text, Jd_text):
    p = '''
    Hello, So suppose you are a Resume Analijer of any company.So , You will be provided a Job description of any 
    opening in comapny.so on the basis of these Job description you need to give the percentage on the resumes
    of the employees.So that it will be easy for the hiring team to schedule interview of best candidate. and
    It will bes best if you give the review on the resume on where candidate need to make changes in the resume
    so that they can get selected.your output in this formate line one should have only percentage on resume.and 
    in second line your review.
    so here is your resume = {resume_text}
    and here is you Job Description = {Jd_text}
    '''
    return p