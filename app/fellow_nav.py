from flask import Blueprint, render_template
import os

# this file a blueprint of our application -> Means it has a bunch of roots inside, has a bunch of URLs defined
# kind of separate our app out, don't have to have all our views defined in one file, can have them defined in multiple files
fellow_nav = Blueprint('fellow_nav', __name__)

# nav
nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]


@fellow_nav.route('/catherine')
def catherine():
    work_info =  [{
            'name': 'Production Engineer Fellow',
            'location': 'MLH',
            'start_date': ' ',
            'end_date': ' ',
            'desc': "The MLH Fellowship is a 12-week internship alternative for aspiring technologists. Fellows on the Production Engineering track experience what it's like to work in Production / Site Reliability Engineering and DevOps."
        },{
            'name': 'Intern',
            'location': '1,000 Dreams Fund',
            'start_date': ' ',
            'end_date': ' ',
            'desc': 'I contribute through both research for outreach and contact building, as well as well as match, pair, and facilitate MentorHER mentorship sessions. '
        },{
            'name': 'Student Advisory Board ',
            'location': '1,000 Dreams Fund',
            'start_date': ' ',
            'end_date': ' ',
            'desc': "I contributed through marketing and was apart of a board that facilitated the scholarship winners for 1000 Dream Fund's student scholarships.  "
        },{
            'name': 'Summer Intern',
            'location': 'Accenture',
            'start_date': ' ',
            'end_date': ' ',
            'desc': "I completed a 6-week survey course focused on introducing the professional culture of global business and topics, skills, and issues that are defining the future of work. I collaborated with 7 interns to create a group project which included a final presentation for Accenture and non-profit guests."
        }]

    education_info = [{
            'name': 'Fresno State University',
            'location': 'Fresno, CA',
            'start_date': 'August 2022',
            'end_date': 'Present',
            'desc': ''
        },{
            'name': 'Sierra Pacific Highschool',
            'location': 'Hanford, CA',
            'start_date': 'August 2018',
            'end_date': 'June 2022',
            'desc': ''
        }]

    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'Kristen', 'url': '/kristen'},
           {'name': 'Helen', 'url': '/helen'},
           {'name': 'Catherine', 'url': '/catherine'}]
    return render_template('./catherine/catherine_page.html', nav=nav, work_info=work_info, education_info=education_info, title="22.SUM.22 Fellow: Catherine Laserna", url=os.getenv("URL"))