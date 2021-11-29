from enum import unique
from app import db


# profile
class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_img=db.Column(db.String(50))
    social_icon_name=db.Column(db.String(50))
    social_icon=db.Column(db.String(50))
    social_icon_url=db.Column(db.String(50))

class ProfileImg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_img=db.Column(db.String(50))

# navbar 

class Navbar(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    navbar_icon_name=db.Column(db.String(50))
    navbar_icon=db.Column(db.String(50))
    navbar_name=db.Column(db.String(50))
    navbar_name_url=db.Column(db.String(50))




class AboutHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_heading_name=db.Column(db.String(50))
    about_txt=db.Column(db.String(50))


class Aboutİmg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_profile_img=db.Column(db.String(50))

class AboutText(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_profile_txt=db.Column(db.String(50))
    about_profile_desc=db.Column(db.String(50))


class AboutInfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    char_start=db.Column(db.String(50))
    char_end=db.Column(db.String(50))




class AboutParag(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    end_txt=db.Column(db.String(50))





class Resume(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    resume_heading=db.Column(db.String(50))
    resume_subheading=db.Column(db.String(50))


class ResumeSumary(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    resume_heading=db.Column(db.String(50))
    resume_subheading=db.Column(db.String(50))
    
    

class Resumedesc(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    resume_desc=db.Column(db.String(50))

class ResumeEdu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    edu_heading=db.Column(db.String(50))
    edu_start_date=db.Column(db.String(50))
    edu_end_date=db.Column(db.String(50))
    edu_txt=db.Column(db.String(50))

    

class Portfolio(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    port_name=db.Column(db.String(50))
    port_desc=db.Column(db.String(50))





class Portfolio_Project(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pr_img=db.Column(db.String(50))
    pr_img_url=db.Column(db.String(50))
    pr_front_name=db.Column(db.String(50))
    pr_front_url=db.Column(db.String(50))
    pr_text=db.Column(db.String(50))
    pr_backend_url=db.Column(db.String(50))
    my_github_url=db.Column(db.String(50))
 

 
class BlogHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_subheading=db.Column(db.String(50))
    blog_heading=db.Column(db.String(50))

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_icon_name=db.Column(db.String(50))
    blog_icon=db.Column(db.String(50))
    blog_link=db.Column(db.String(50))
    blog_head=db.Column(db.String(50))
    blog_txt=db.Column(db.String(50))




class ContactHeading(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     contact_subheading_name=db.Column(db.String(50))
     contact_heading_name=db.Column(db.String(50))




class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_icon=db.Column(db.String(50))
    contact_icon_txt=db.Column(db.String(50))
    contact_desc=db.Column(db.String(50))
    contact_link=db.Column(db.String(50))







class ContactMe(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_message=db.Column(db.Text)












































































