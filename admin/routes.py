
from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect
from flask import url_for
import os
# from flask_bcrypt import Bcrypt
def loginCheck(param):
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return param
    else:
               return redirect(url_for('login'))

@app.route('/admin')
def admin_index():
   profiles=Profile.query.all()
   navs=Navbar.query.all()
   aboutheads=AboutHeading.query.all()
   abouts=AboutHeading.query.all()
   resus=Resume.query.all()
   sums=ResumeSumary.query.all()
   descs=Resumedesc.query.all()
   posts=Aboutİmg.query.all()
   texts=AboutText.query.all()
   words=AboutInfo.query.all()
   txts=AboutParag.query.all()
   items=ResumeEdu.query.all()
   ports=Portfolio.query.all()
   links=Portfolio_Project.query.all()  
   blogheads=BlogHeading.query.all()
   blogs=Blog.query.all()
   contacts=ContactHeading.query.all
   icons=Contact.query.all()
   return loginCheck(render_template('admin/index.html', profiles=profiles,navs=navs,aboutheads=aboutheads,abouts=abouts,resus=resus,   
   sums=sums,descs=descs,posts=posts,texts=texts,words=words,txts=txts, items=items , ports=ports,links=links,blogheads=blogheads, blogs=blogs ,contacts=contacts, icons=icons))
  

# profile

@app.route('/admin/profile', methods=['GET','POST']) 
def profile():
   profiles=Profile.query.all()
   if request.method=='POST':
      profile=Profile(
         social_icon_name=request.form['social_icon_name'],
         social_icon=request.form['social_icon'],
         social_icon_url=request.form['social_icon_url']

      )     
      db.session.add(profile)
      db.session.commit()
      return redirect('/admin/profile')
   return loginCheck(render_template('admin/profile.html',profiles=profiles))

# delete
@app.route("/admin/profiledelete/<id>")
def profileldelete(id):
   profile=Profile.query.get(id)
   db.session.delete(profile)
   db.session.commit()
   return redirect('/admin/profile')


# update
@app.route("/admin/profileupdate/<id>" , methods=['GET','POST']) 
def profileupdate(id):
   profile=Profile.query.get(id)
   if request.method=='POST':
      profile.social_icon_name=request.form['social_icon_name']
      profile.social_icon=request.form['social_icon']
      profile.social_icon_url=request.form['social_icon_url']
      db.session.commit()
      return redirect('/admin/profile')
   return loginCheck(render_template('admin/profileupdate.html',profile=profile))

#  end


#  navbar

@app.route('/admin/navbar', methods=['GET','POST']) 
def nav():
   navs=Navbar.query.all()
   if request.method=='POST':
      nav=Navbar(
      navbar_icon_name=request.form['navbar_icon_name'],
      navbar_icon=request.form['navbar_icon'],
      navbar_name=request.form['navbar_name'],
      navbar_name_url=request.form['navbar_name_url']

      )     
      db.session.add(nav)
      db.session.commit()
      return redirect('/admin/navbar')
   return loginCheck(render_template('admin/navbar.html',navs=navs))
   
   
@app.route("/admin/navbardelete/<id>")
def navdelete(id):
   nav=Navbar.query.get(id)
   db.session.delete(nav)
   db.session.commit()
   return redirect('/admin/navbar')

@app.route("/admin/navbarupdate/<id>" , methods=['GET','POST'])  
def navbarupdate(id):
    nav=Navbar.query.get(id)
    if request.method=='POST':
      nav.navbar_icon_name=request.form['navbar_icon_name']
      nav.navbar_icon=request.form['navbar_icon']
      nav.navbar_name=request.form['navbar_name']
      nav.navbar_name_url =request.form['navbar_name_url']
      db.session.commit()
      return redirect('/admin/navbar')
    return loginCheck(render_template('admin/navbarupdate.html',nav=nav))

# end

# aboutheading


@app.route('/admin/aboutheading', methods=['GET','POST']) 
def adminAboutHeading():
   aboutheads=AboutHeading.query.all()
   if request.method=='POST':
      abouthead=AboutHeading(
         about_heading_name=request.form['about_heading_name'],
         about_txt=request.form['about_txt']
      )     
      db.session.add(abouthead)
      db.session.commit()
      return redirect('/admin/aboutheading')
   return loginCheck(render_template('admin/aboutheading.html',aboutheads=aboutheads))
   
@app.route("/admin/aboutheadingdelete/<id>")
def aboutheadingdelete(id):
   abouthead=AboutHeading.query.get(id)
   db.session.delete(abouthead)
   db.session.commit()
   return redirect('/admin/aboutheading')


@app.route("/admin/aboutheadingupdate/<id>" , methods=['GET','POST'])  
def aboutheadingupdate(id):
   abouthead=AboutHeading.query.get(id)
   if request.method=='POST':
      abouthead.about_heading_name=request.form['about_heading_name']
      abouthead.about_txt=request.form['about_txt']
      db.session.commit()
      return redirect('/admin/aboutheading')
   return loginCheck(render_template('admin/aboutheadingupdate.html',abouthead=abouthead))

# end



# about img
@app.route('/admin/aboutimg', methods=['GET','POST']) 
def aboutimg():
   posts=Aboutİmg.query.all()
   if request.method=='POST':
      file=request.files['about_profile_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post=Aboutİmg(
       about_profile_img=filename

      )     
      db.session.add(post)
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck(render_template('admin/aboutimg.html',posts=posts))

# delete
@app.route("/admin/aboutimgdelete/<id>")
def Aboutimgdelete(id):
   post=Aboutİmg.query.get(id)
   db.session.delete(post)
   db.session.commit()
   return redirect('/admin/aboutimg')


# update
@app.route("/admin/aboutimgupdate/<id>" , methods=['GET','POST']) 
def Aboutimgupdate(id):
   post=Aboutİmg.query.get(id)
   if request.method=='POST':
      file=request.files['about_profile_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      post.about_profile_img=filename
      db.session.commit()
      return redirect('/admin/aboutimg')
   return loginCheck(render_template('admin/aboutimgupdate.html',post=post))

#  end

# about text
@app.route('/admin/aboutext', methods=['GET','POST']) 
def text():
   texts=AboutText.query.all()
   if request.method=='POST':
      text=AboutText(
      about_profile_txt=request.form['about_profile_txt'],
      about_profile_desc=request.form['about_profile_desc'],

      )     
      db.session.add(text)
      db.session.commit()
      return redirect('/admin/aboutext')
   return loginCheck(render_template('admin/aboutext.html',texts=texts))
   
@app.route("/admin/aboutextdelete/<id>")
def textdelete(id):
   text=AboutText.query.get(id)
   db.session.delete(text)
   db.session.commit()
   return redirect('/admin/aboutext')


@app.route("/admin/aboutextupdate/<id>" , methods=['GET','POST'])  
def textupdate(id):
   text=AboutText.query.get(id)
   if request.method=='POST':
      text.about_profile_txt=request.form['about_profile_txt']
      text.about_profile_desc=request.form['about_profile_desc']
   
      db.session.commit()
      return redirect('/admin/aboutext')
   return loginCheck(render_template('admin/aboutextupdate.html',text=text))


# 

# About info
@app.route('/admin/aboutinfo', methods=['GET','POST']) 
def info():
   words=AboutInfo.query.all()
   if request.method=='POST':
      word=AboutInfo(
      char_start=request.form['char_start'],
      char_end=request.form['char_end'],

   
      )     
      db.session.add(word)
      db.session.commit()
      return redirect('/admin/aboutinfo')
   return loginCheck(render_template('admin/aboutinfo.html',words=words))
   
@app.route("/admin/aboutinfodelete/<id>")
def infodelete(id):
   word=AboutInfo.query.get(id)
   db.session.delete(word)
   db.session.commit()
   return redirect('/admin/aboutinfo')


@app.route("/admin/aboutinfoupdate/<id>" , methods=['GET','POST'])  
def infoupdate(id):
   word=AboutInfo.query.get(id)
   if request.method=='POST':
      word.char_start=request.form['char_start']
      word.char_end=request.form['char_end']
   
    
      db.session.commit()
      return redirect('/admin/aboutinfo')
   return loginCheck(render_template('/admin/aboutinfoupdate.html',word=word))





# about end desc
@app.route('/admin/rend', methods=['GET','POST']) 
def rend():
   txts=AboutParag.query.all()
   if request.method=='POST':
      txt=AboutParag(
       end_txt=request.form['end_txt']
    
      )     
      db.session.add(txt)
      db.session.commit()
      return redirect('/admin/rend')
   return loginCheck(render_template('admin/rend.html',txts=txts))
   
   # update
@app.route("/admin/rendupdate/<id>" , methods=['GET','POST'])  
def rendupdate(id):
   txt=AboutParag.query.get(id)
   if request.method=='POST':
      txt.end_txt=request.form['end_txt']
      db.session.commit()
      return redirect('/admin/rend')
   return loginCheck(render_template('admin/rendupdate.html',txt=txt))

@app.route("/admin/renddelete/<id>")
def renddelete(id):
   txt=AboutParag.query.get(id)
   db.session.delete(txt)
   db.session.commit()
   return redirect('/admin/rend')

# about edu

@app.route('/admin/edu', methods=['GET','POST']) 
def edu():
   items=ResumeEdu.query.all()
   if request.method=='POST':
      item=ResumeEdu(
      edu_heading=request.form['edu_heading'],
      edu_start_date=request.form['edu_start_date'],
      edu_end_date=request.form['edu_end_date'],
      edu_txt=request.form['edu_txt']
      )     
      
      db.session.add(item)
      db.session.commit()
      return redirect('/admin/edu')
   return loginCheck(render_template('admin/edu.html',items=items))
   
   # update
@app.route("/admin/eduupdate/<id>" , methods=['GET','POST'])  
def eduupdate(id):
   item=ResumeEdu.query.get(id)
   if request.method=='POST':
      item.edu_heading=request.form['edu_heading']
      item.edu_start_date=request.form['edu_start_date']
      item.edu_end_date=request.form['edu_end_date']
      item.edu_txt=request.form['edu_txt']

      db.session.commit()
      return redirect('/admin/edu')
   return loginCheck(render_template('admin/eduupdate.html',item=item))

@app.route("/admin/edudelete/<id>")
def edudelete(id):
   item=ResumeEdu.query.get(id)
   db.session.delete(item)
   db.session.commit()
   return redirect('/admin/edu')

# 


# resume heading

@app.route('/admin/resumeheading', methods=['GET','POST']) 
def resumeheading():
   resus=Resume.query.all()
   if request.method=='POST':
      resu=Resume(
       resume_heading=request.form['resume_heading'],
       resume_subheading=request.form['resume_subheading']
      )     
      db.session.add(resu)
      db.session.commit()
      return redirect('/admin/resumeheading')
   return loginCheck(render_template('admin/resumeheading.html',resus=resus))
   
   # update
@app.route("/admin/resumeheadingupdate/<id>" , methods=['GET','POST'])  
def resumeheadingupdate(id):
   resu=Resume.query.get(id)
   if request.method=='POST':
      resu.resume_heading=request.form['resume_heading']
      resu.resume_subheading=request.form['resume_subheading']
      db.session.commit()
      return redirect('/admin/resumeheading')
   return loginCheck(render_template('admin/resumeheadingupdate.html',resu=resu))

@app.route("/admin/resumeheadingdelete/<id>")
def resumeheadingdelete(id):
   resu=Resume.query.get(id)
   db.session.delete(resu)
   db.session.commit()
   return redirect('/admin/resumeheading')

# resume Sum
@app.route('/admin/rsum', methods=['GET','POST']) 
def rsum():
   sums=ResumeSumary.query.all()
   if request.method=='POST':
      sum=ResumeSumary(
      resume_heading=request.form['resume_heading'],
      resume_subheading=request.form['resume_subheading'],

   
      )     
      db.session.add(sum)
      db.session.commit()
      return redirect('/admin/rsum')
   return loginCheck(render_template('admin/rsum.html',sums=sums))
   
@app.route("/admin/rsumdelete/<id>")
def rsumdelete(id):
   sum=ResumeSumary.query.get(id)
   db.session.delete(sum)
   db.session.commit()
   return redirect('/admin/rsum')


@app.route("/admin/rsumupdate/<id>" , methods=['GET','POST'])  
def rsumupdate(id):
   sum=ResumeSumary.query.get(id)
   if request.method=='POST':
      sum.resume_heading=request.form['resume_heading']
      sum.resume_subheading=request.form['resume_subheading']
    

      db.session.commit()
      return redirect('/admin/rsum')
   return loginCheck(render_template('admin/rsumupdate.html',sum=sum))


# 

# resume desc

@app.route('/admin/rdesc', methods=['GET','POST']) 
def rdesc():
   descs=Resumedesc.query.all()
   if request.method=='POST':
      desc=Resumedesc(
      resume_desc=request.form['resume_desc']
    
      )     
      db.session.add(desc)
      db.session.commit()
      return redirect('/admin/rdesc')
   return loginCheck(render_template('admin/rdesc.html',descs=descs))
   
   # update
@app.route("/admin/rdescupdate/<id>" , methods=['GET','POST'])  
def rdescupdate(id):
   desc=Resumedesc.query.get(id)
   if request.method=='POST':
      desc.resume_desc=request.form['resume_desc']
      db.session.commit()
      return redirect('/admin/rdesc')
   return loginCheck(render_template('admin/rdescupdate.html',desc=desc))

@app.route("/admin/rdescdelete/<id>")
def rdescdelete(id):
   desc=Resumedesc.query.get(id)
   db.session.delete(desc)
   db.session.commit()
   return redirect('/admin/rdesc')

# 

 

# Portfolio heading
@app.route('/admin/port', methods=['GET','POST']) 
def port():
   ports=Portfolio.query.all()
   if request.method=='POST':
      port=Portfolio(
       port_name=request.form['port_name'],
       port_desc=request.form['port_desc']
      )     
      db.session.add(port)
      db.session.commit()
      return redirect('/admin/port')
   return loginCheck(render_template('admin/port.html',ports=ports))
   
   # update
@app.route("/admin/portupdate/<id>" , methods=['GET','POST'])  
def portupdate(id):
   port=Portfolio.query.get(id)
   if request.method=='POST':
      port.port_name=request.form['port_name']
      port.port_desc=request.form['port_desc']
      db.session.commit()
      return redirect('/admin/port')
   return loginCheck(render_template('admin/portupdate.html',port=port))

@app.route("/admin/portdelete/<id>")
def portdelete(id):
   port=Portfolio.query.get(id)
   db.session.delete(port)
   db.session.commit()
   return redirect('/admin/port')




# portfolio img

@app.route('/admin/pt', methods=['GET','POST']) 
def portfolio():
   links=Portfolio_Project.query.all()
   if request.method=='POST':
      file=request.files['pr_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link=Portfolio_Project(
         pr_front_name=request.form['pr_front_name'],
         pr_front_url =request.form['pr_front_url'],
         pr_img_url=request.form['pr_img_url'],
         pr_text=request.form['pr_text'],
         pr_backend_url=request.form['pr_backend_url'],
         my_github_url=request.form['my_github_url'],
         pr_img=filename

      )     
      db.session.add(link)
      db.session.commit()
      return redirect('/admin/pt')
   return loginCheck(render_template('admin/pt.html',links=links))

# delete
@app.route("/admin/ptdelete/<id>")
def porfoliodelete(id):
   link=Portfolio_Project.query.get(id)
   db.session.delete(link)
   db.session.commit()
   return redirect('/admin/pt')


# update
@app.route("/admin/ptupdate/<id>" , methods=['GET','POST']) 
def portfolioupdate(id):
   link=Portfolio_Project.query.get(id)
   if request.method=='POST':
      file=request.files['pr_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      link.pr_img_url==request.form['pr_img_url']
      link.pr_front_name==request.form['pr_front_name']
      link.pr_front_url==request.form['pr_front_url']
      link.pr_text==request.form['pr_text']
      link.pr_backend_url==request.form['pr_backend_url']
      link.my_github_url==request.form['my_github_url']
      link.pr_img=filename
      db.session.commit()
      return redirect('/admin/pt')
   return loginCheck(render_template('admin/ptupdate.html',link=link))

#  end


# bloghead

@app.route('/admin/bloghead', methods=['GET','POST']) 
def bloghead():
   blogheads=BlogHeading.query.all()
   if request.method=='POST':
      bloghead=BlogHeading(
       blog_subheading=request.form['blog_subheading'],
       blog_heading=request.form['blog_heading']
      )     
      db.session.add(bloghead)
      db.session.commit()
      return redirect('/admin/bloghead')
   return loginCheck(render_template('admin/bloghead.html',blogheads=blogheads))
   
   # update
@app.route("/admin/blogheadupdate/<id>" , methods=['GET','POST'])  
def blogheadupdate(id):
   bloghead=BlogHeading.query.get(id)
   if request.method=='POST':
      bloghead.blog_heading=request.form['blog_heading']
      bloghead.blog_subheading=request.form['blog_subheading']
      db.session.commit()
      return redirect('/admin/bloghead')
   return loginCheck(render_template('admin/blogheadupdate.html',bloghead=bloghead))

@app.route("/admin/blogheaddelete/<id>")
def blogheaddelete(id):
   bloghead=BlogHeading.query.get(id)
   db.session.delete(bloghead)
   db.session.commit()
   return redirect('/admin/bloghead')

# 

#blog

@app.route('/admin/blog', methods=['GET','POST']) 
def blog():
   blogs=Blog.query.all()
   if request.method=='POST':
      blog=Blog(
      blog_icon_name=request.form['blog_icon_name'],
      blog_icon=request.form['blog_icon'],
      blog_link=request.form['blog_link'],
      blog_head=request.form['blog_head'],
      blog_txt=request.form['blog_txt']

   
      )     
      db.session.add(blog)
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck(render_template('admin/blog.html',blogs=blogs))
   
@app.route("/admin/blogdelete/<id>")
def blogdelete(id):
   blog=Blog.query.get(id)
   db.session.delete(blog)
   db.session.commit()
   return redirect('/admin/blog')


@app.route("/admin/blogupdate/<id>" , methods=['GET','POST'])  
def blogupdate(id):
   blog=Blog.query.get(id)
   if request.method=='POST':
      blog.blog_icon_name=request.form['blog_icon_name']
      blog.blog_icon=request.form['blog_icon']
      blog.blog_link=request.form['blog_link']
      blog.blog_head=request.form['blog_head']
      blog.blog_txt=request.form['blog_txt']
    
      db.session.commit()
      return redirect('/admin/blog')
   return loginCheck(render_template('admin/blogupdate.html',blog=blog))


#  

# contactheading

@app.route('/admin/contactheading', methods=['GET','POST']) 
def contactheading():
   contacts=ContactHeading.query.all()
   if request.method=='POST':
      contact=ContactHeading(
      contact_subheading_name =request.form['contact_subheading_name'],
      contact_heading_name=request.form['contact_heading_name']
      )     
      db.session.add(contact)
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck(render_template('admin/contactheading.html',contacts=contacts))
   
   # update
@app.route("/admin/contactheadingupdate/<id>" , methods=['GET','POST'])  
def contactupdate(id):
   contact=ContactHeading.query.get(id)
   if request.method=='POST':
      contact.contact_subheading_name=request.form['contact_subheading_name']
      contact.contact_heading_name=request.form['contact_heading_name']
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck(render_template('admin/contactheadingupdate.html',contact=contact))

@app.route("/admin/contactheadingdelete/<id>")
def contactdelete(id):
   contact=ContactHeading.query.get(id)
   db.session.delete(contact)
   db.session.commit()
   return redirect('/admin/contactheading')

# end

# icon

@app.route('/admin/icon', methods=['GET','POST']) 
def icon():
   icons=Contact.query.all()
   if request.method=='POST':
      icon=Contact(
      contact_icon=request.form['contact_icon'],
      contact_icon_txt=request.form['contact_icon_txt'],
      contact_desc=request.form['contact_desc'],
      contact_link=request.form['contact_link']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/icon.html',icons=icons))
   
   # update
@app.route("/admin/iconupdate/<id>" , methods=['GET','POST'])  
def iconupdate(id):
   icon=Contact.query.get(id)
   if request.method=='POST':
      icon.contact_icon=request.form['contact_icon']
      icon.contact_icon_txt=request.form['contact_icon_txt']
      icon.contact_desc=request.form['contact_desc']
      icon.contact_link=request.form['contact_link']

      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/iconupdate.html',icon=icon))

@app.route("/admin/icondelete/<id>")
def icondelete(id):
   icon=Contact.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/icon')

# end













