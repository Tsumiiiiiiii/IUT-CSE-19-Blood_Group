from flask import Flask,request
from bdgp import get

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method=='POST':
        opt=request.form.get('bldgrp')
        inf=get(opt)
        s='''
        <html>
        <body>
        '''
        s+='''
        <p style = "font-family:candara">The matches with blood group {} ({} matches) are as follows: </p></br>'''.format(opt,len(inf))
        for people in inf:
            s=s+'''
            <pre>NAME                  :  {name}</pre>'''.format(name=people[0].upper())
            if(people[1]=="Not given"):
                s+='''
                <pre>MOBILE                :  NOT GIVEN</pre>'''
            else:
                s+='''
                <pre>MOBILE                :  <a href="tel:{mobile}">{mobile}</a></pre>'''.format(mobile=people[1])
            s+='''
            <pre>EMAIL                 :  <a href="mailto:{email}">{email}</a></pre>
            <pre>.......................................................................</pre>
            '''.format(email=people[2])
        s+='''
        </body>
        </html>
        '''
        return s
    return '''
    <html>
    <head>
        <style>
        form     {
                position:fixed;
                top:35%;
                left:40%;
                width:550px;
    }
        </style>
    </head>
        <body>
            <form method="POST" action=".">
            <h3 style = "font-family:candara">SELECT THE BLOOD GROUP : </h3>
            <select id="bldgrp" name="bldgrp">
                <option value="A+">A+</option>
                <option value="B+">B+</option>
                <option value="AB+">AB+</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
            </select>
            <button class="btn btn-default" type="submit">Submit</button>
            </br>
            <p style = "font-family:candara"><b>N.B. </b>No matches for blood groups A- , B- , AB-</p>
            </form>
        </body>
    </html>'''
