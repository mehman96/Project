# from re import M, T
from admin.routes import *
from app import app
from app.models import *
from flask import render_template,request,redirect





@app.route('/')
def index():
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
    contacts=ContactHeading.query.all()
    icons=Contact.query.all()
    return render_template('main/index.html',profiles=profiles,navs=navs,aboutheads=aboutheads,abouts=abouts,sports=ports
    ,posts=posts, texts=texts, words=words, txts=txts,items=items, ports= ports,links=links ,blogheads=blogheads,blogs=blogs, resus=resus,sums=sums,descs=descs,contacts=contacts,icons=icons)


@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   contactforms =ContactMe.query.all()
   if request.method=='POST':
      contactform=ContactMe(
   user_name=request.form['user_name'],
   user_email=request.form['user_email'],
   user_message=request.form['user_message']

      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/')
   return loginCheck (render_template('admin/contactform.html',contactforms=contactforms ))
   
@app.route("/admin/contactformdelete/<id>")
def contactformdelete(id):
   contactform =ContactMe.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect('/admin/contactform')



 
   