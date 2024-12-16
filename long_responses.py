import random

R_EATING = "I don't  eat anything because I'm a bot obviously!"
R_FACULTYLOGIN ="https://specexams.in/BeesErp/Login.aspx"
R_STUDENTLOGIN="https://specexams.in/BeesErp/Login.aspx"
R_COURSE = "Courses like CSE,ECE,EEE,MECH,IT,AIDS in the college"
R_HOD = "name of hod cse department Dr.DILEEP"
R_DEPARTMENT = "CSE,EEE,ECE,IT,CIVIL,MECHANICAL,AIDS"
R_PLACEMENTOFFICER = "placement officer of this college is Dr.K.SRIKANTH"
R_PRINCIPALNAME = "Dr.K.Sree Latha"
R_STUDENTCOUNT = "there are 198 students in cse department"
R_LAB = "3 Labs that are i)data science ii)Artificial intelligence iii)IOT "
R_SYSTEM = "There are 150 system in cse department"
R_PLACEMENTCOMPANY = "Amazon,Wipro,Accenture,Tech Mahindra"
R_COLLEGELOCATION="College is located at Opp. Forest Academy, Kompally Road, Dullapally, Maisammaguda, Medchal, Hyderabad - 500100, Telangana, India."
R_FEESSTRUCTURE="For management quota = 100000,For Government quota = 50000"
R_STUDENTPLACEMENT="There are totally 540 students are placed in various companies"


def unknown():
    response = ["Could you kindly reword that query? ",
                "Can you phrase your question in another way?",
		"If your query is not resolved yet, you can contact Phone:+91                  9000008578 E-mail:principal@stpetershyd.com"][
        random.randrange(4)]
    return response