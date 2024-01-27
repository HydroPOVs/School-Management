import os
import webbrowser

from ABC.pages import header

class career():

    def __init__(self) -> None:
        self.Employment_Form = os.path.join(os.getcwd(), "ABC", "docs", "Employment Application 2024-25.pdf")
        
        header()
        print()
        self.main_page()

    def main_page(self):
        print ("""
    Work Culture at  A B C Institute of Technology:- 
            The work culture at  A B C Institute of Technology(ABCIT) is based on simple but the most powerful philosophy – “Commitment”. This honest philosophy comes from the Founder and Chairman of the Institute. Since his erstwhile days, the Chairman has laid prime emphasis on commitment at work. Every associate at ABCIT understand the significance of commitment in bringing innovation in what one does, and acknowledges it completely. This work culture equips an employee at  A B C Institute of Technology to work with utmost dedication in whatever job is given to him/her.

            Team work amongst the employees is the second most vital characteristics in making  A B C Institute of Technology a success story nationwide. A student can only get a thorough and flawless study material and classroom lecture, if the team which has worked behind it is efficient. Work hard and party harder is the motto at  A B C Institute of Technology. When it comes to fun-filled evenings, the employees make sure that the spirits touch the ceiling and turn jubilant to enjoy the fruits of hard work.

    Attitude and Skill Sets in Requisition

        At A B C Institute of Technology, we believe that attitude is what makes a person successful and not lone skills. The search for a perfect for ABCIT starts at analyzing the attitude of the candidate. Skills, however, are something which can be developed as per the requirement. Conversely, if the right attitude is not there in candidates, who are seeking entry into A B C Institute of Technology, then this is certainly not the place for them.

        To be successful, an organization needs to identify the problem areas which exist. More often than not, the resolution to the problem lies with hiring the right resource, which has the capabilities to work out the solution for the organization. The problem can be perceived as a lock and the resource can be perceived as a key. Unless and until, the key is right, it will not open the lock, similar to a business situation where a business issue will not be solved unless the right resource works on it. Similarly,  A B C Institute of Technology looks for the perfect key to open (solve) the lock (problems) which comes in its way to achieve even greater heights.

                    "We are a demanding and highly supportive employer"

        A B C Institute of Technology offers compensation, which is not only higher than the industry standards but also illimitable for deserving candidates. It offers an entrepreneurial environment along with corporate outlook in a right mix to help its employees grow in all three dimensions: Money – Career – Intellect.

        To ensure a smooth induction, ABCIT offers a specialized induction program for its teaching and non-teaching staffs. Institute has a well defined employee development and support system. Our years of operational experience has helped us identify following attitudinal traits, which forms scale for selecting associates:

    Commitment and Dedication

            Team player
            Loyalty and Reliability
        Passion and zeal to excel
        Leadership
        Systematic approach
        Industriousness
        Fun-loving
    

    How to Apply:

        For Non-Academics Positions: Please mail cv at nonacad.rct@abcit.in
        For Academic Positions: Please mail cv at acad.career@abcit.in
    

    Teaching Staff -

        A candidate who:

        Aspires to make a career in teaching
        Has command over subject matter
        Has good command over spoken English
        Has a winning attitude and appetite to face challenge
        Has sincerity in actions and commitment in outlook
        Needs an honest, transparent and supportive work culture which promotes talent

    Desired Profiles (for Academic Positions):

        A P.hd (Botany / Zoology / Physics / Chemistry / Mathematics) candidate graduated recently and is looking for opportunities in  training arena. Candidates already teaching in the training industry and has good success rate.

                                OR

        Expert teachers in Botany / Zoology / Physics / Chemistry / Mathematics working at any other training institute for preparing students and is keen to work in highly motivated & systematic environment.	

                                OR
        
        Faculty members at IITs / reputed Colleges / Universities, who are keen to work in a highly motivated & organized environment of Medical and Engineering Entrance training.

    Non-Academic Staff -

        A candidate who:

        Aspires to make a career in booming education industry
        Has skills which can dwarf competition
        Has excellent communication skills
        Has a winning attitude and appetite to face challenge
        Has sincerity in actions and commitment in outlook
        Needs an honest, transparent and supportive work culture which promotes talent
    

    Desired Profiles (for Managerial Positions):

        A post graduate / MBA from a premier management school and are looking for opportunities in  training arena. Candidates with prior experience in education industry will be preferred.

                                OR

        A graduate with 5-6 years of experience in business development, marketing and corporate sales working at any other training institute and is keen to work in highly motivated & higher-growth-oriented environment.

                                OR

        A graduate, who is keen to work in a highly motivated & higher-growth-oriented environment and wants to establish strong work credentials.

    GROWTH OPPORTUNITIES:

        Work Streams for Academic Staff:

        Classroom Teaching: Good lectureship skills for classroom teaching 
        Content Development: Skills in content development for books, study material, test papers and online programs
        Centre Management: Manage a team of teachers and administrative staff as an independent centre head
        Business Development: Lead a team of academicians for promotion programs and workshops
    

    Work Streams for Non-Academic Staff:

        Sales & Marketing:

        Business Development: Lead a team of executives for School programs, Workshops, Campus initiatives, etc.
        Brand Development: Promotion and events management, Road shows, School programs etc.
        Centre Management: Manage a team of Executives and administrative staff independently
        Special Projects: Franchise Assignments, Contact Programs, etc.
    

    WHAT WE OFFER:

        An Excellent Salary
        Great Career Path
        Intellectual Growth
        Personal Development
        Leadership Opportunity

    Post Date      Job Id	            Designation                                        
    Dec 03, 2019	 F0MPCHB	 Foundations Faculty	               
    Dec 03, 2019	 AC04P	 	 Physics Faculty (Engineering)	                
    Dec 03, 2019	 AC04C		 Chemistry Faculty (Engineering)	               
    Dec 03, 2019	 AC04M		 Mathematics Faculty (Engineering)              
    Dec 03, 2019	 AC05C		 Chemistry Faculty (Medical)	               
    Dec 03, 2019	 AC05B		 Botany Faculty (Medical)	               
    Dec 03, 2019	 AC05Z		 Zoology Faculty (Medical)	                 
    Dec 03, 2019	 AC05P		 Physics Faculty (Medical)	               
    Dec 03, 2019	 AE01		 Accounts Executive	                                 
    Dec 03, 2019	 AD01		 Admin Executive	                                 
    Dec 03, 2019	 CS01		 Counsellor	                                 
    Dec 03, 2019	 ED01		 EDP Executive	                                 """)
        
        print()
        menu_options = [
            ("APPLICATION FORM", "1"),
            ("GO TO BACK", "2"),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
        
        print()
        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            webbrowser.open(self.Employment_Form)