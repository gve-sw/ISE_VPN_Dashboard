from flask import Flask, render_template, request, redirect, url_for
from apiISE import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("iseIndex.html")

@app.route('/viewUsers',methods=['GET','POST'])
def viewUsers():
    username=getUsers()
    text=username.json()
    userInformation=[]
    for i in text['SearchResult']['resources']:
        singleUser=getSingleUser(i['id'])
        singleUserText=singleUser.json()
        enableStatus=singleUserText['InternalUser']['enabled']
        userInformation.append({'name':i['name'],'id':i['id'],'description':i['description'],'enabled':enableStatus})
    return render_template("viewUsers.html",user=userInformation)

@app.route('/newUser',methods=['GET','POST'])
def newUser():
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        enable = request.form['enable']
        description = request.form['description']
        result=createNewUser(name,password,enable,description)
        return redirect(url_for('result',result=result,typeOf='new_user',name=name,enable=enable))
    return render_template("newUser.html")

@app.route('/editUser',methods=['GET','POST'])
def editUser():
    user = request.args.get('user', None)
    idvar = request.args.get('idvar',None)
    if request.method == "POST":
        enable = request.form['enable']
        result=modifyUser(user,idvar,enable)
        return redirect(url_for('result',result=result,typeOf="edit_user",name=user,enable=enable))
    return render_template("editUser.html",name=user)

@app.route('/result',methods=['GET','POST'])
def result():
    result=request.args['result']
    typeOf=request.args['typeOf']
    name=request.args['name']
    enable=request.args['enable']
    if typeOf == "new_user":
        if result == "<Response [201]>":
            message = 'Successfully created "'+name+'" with Enabled: '+enable
            return render_template('result.html',message=message)
        else:
            message='Error with response code "'+result+'"'
            return render_template('result.html',message=message)
    elif typeOf == "edit_user":
        if result=="<Response [200]>":
            message='User "'+name+'" now has Enabled: '+enable
            return render_template('result.html',message=message)
        else:
            message='Error with response code "'+result+'"'
            return render_template('result.html',message=message)
    return render_template('iseIndex.html')


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.debug=True
    app.run()
