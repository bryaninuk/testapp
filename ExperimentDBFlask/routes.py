from flask import Flask, url_for, render_template, request # url_for= for defining a link. request= forms. render_t= jinja

from app import app; # first app pionts to app file app.py second app is name of variable declared in app.py code
import redis;
r= redis.StrictRedis(host='localhost',port=6379,db=0, charset="utf-8", decode_responses=True); #Connect to redis (charset="utf-8", decode_responses=true brings back data as string instead of bytes)


# server/
@app.route('/')
def link():

    return render_template('start.html')

    #createlink = "<a href='" + url_for('create') + "'>ADD A RECORD</a>"; # Define the link for create page link will always be correct for create even if it changes in app.rout (create)
    #return ( createlink) #Createlink writes the link

    #createlink2 = "<a href='" + url_for('record') + "'>Search Record</a>"; # Define the link for create page link will always be correct for create even if it changes in app.rout (create)
    #return ( createlink2) #Createlink writes the link

#server/CREATE RECORD
@app.route('/create', methods= ['GET', 'POST'])
def create():
     if request.method == 'GET': 
          return render_template('SaveRecord.html'); # send user the form to input text
     elif request.method == 'POST': 
        bird = request.form['bird']; # read form data and save it
        idnotes = request.form['idnotes'];  #these (red) are the names of the text boxes in the html black is variable
        distribution = request.form['distribution'];

        r.set(bird + ' :bird', bird) # colone signifies key but is not essential its a covention...key= what is jelly:question
        r.set(bird + ' :idnotes', idnotes)
        r.set(bird + ' :distribution', distribution)

        return render_template('createdrecord.html', birdadded=bird ); # birdadded is variable from html text
     else:
           return "<h2>Invalid request!</h2>";


#server/READ RECORD

@app.route('/record', methods= ['GET', 'POST'])
def record(): 
        
    if request.method == 'GET': 
        return render_template('inputbird.html') #send user the form to get name of bird
    elif request.method == 'POST': 
        title = request.form['title'];# read text from form data

         #read question from data store
        bird = r.get(title+' :bird')
        idnotes = r.get(title+' :idnotes')
        distribution= r.get(title+' :distribution')
        return render_template('search.html', birdhtml= bird, idnoteshtml=idnotes, distributionhtml=distribution );
    else:
           return "<h2>Invalid request!</h2>";   
        
       
               