from flask import Flask,render_template,request,session
import random

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/',methods=['GET',"POST"])
def gamepage():
    if request.method=='POST':
        uc = request.form['uchoice']  
        caldata = calculation(uc) 
        
        return render_template('gamepage.html',caldata=caldata) 

    session.pop('cpts', None)  
    session.pop('upts', None) 

    result = {'user':'','comp':'','upts':0,'cpts':0,'pt':'','won':''}
    return render_template('gamepage.html',caldata=result)


def calculation(uc):
    user = uc 
    game= {1:'stone' , 2:'paper' , 3:'scissor'}
    comp = game[random.randint(1,3)]

    try:
        cpts = session['cpts']
        upts = session['upts']

    except KeyError:
        cpts = upts= 0

    pt= ''
      
    while ( (cpts <= 3) and (upts <= 3) ):
        if ( (user=='stone')and (comp=='paper') ):
            cpts = cpts + 1
            pt   = "Comp 1 point"
        elif ( (user=='stone')and (comp=='scissor') ):
            upts = upts + 1
            pt   = "player 1 point"
        elif ( (user=='paper')and (comp=='scissor') ):
            cpts = cpts + 1
            pt   = "Comp 1 point"
        elif ( (user=='paper')and (comp=='stone') ):
            upts = upts + 1
            pt   = "player 1 point"

        elif ( (user=='scissor')and (comp=='stone') ):
            cpts = cpts + 1
            pt   = "Comp 1 point"
        elif ( (user=='scissor')and (comp=='paper') ):
            upts = upts + 1
            pt   = "player 1 point"
        elif ( user == comp ):
            upts = upts + 0.5
            cpts = cpts + 0.5
            pt   = "Both half Point"
        break
    
    session['cpts'] = cpts
    session['upts'] = upts
    result = {'user':uc,'comp':comp,'upts':upts,'cpts':cpts,'pt':pt}    

    if (cpts>=3) :
        won = "Computer have won the game"
        result['won']=won

    elif (upts>=3) :
        won = "Player have won the game" 
        result['won']=won 

    elif ((upts>=3) & (cpts>=3)) :
        won = "Match tie" 
        result['won']=won

    else:
        won="" 
        result['won']=won
       
    return result
    

    

       
if __name__ == '__main__':
    app.run(debug=True)
    
    
'''
flask Module to use Flask frame work.
Here  Session is used to save the data locally.
Random was the function used to generate numbers randomly.

This game is based on prediction of events.
Based on the Points gained winner is decided.
Here the Player who scored above 3points are considered as winner.
If both plays the same option then half point will be credited to both.


'''
