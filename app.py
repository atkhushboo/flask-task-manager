from flask import Flask ,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# --------initializ objects--------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


# ------Todo Class-------
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) ->str:
        return f"{self.sno} {self.title}"

@app.route("/",methods=["GET","POST"])
def main():
    if request.method=="POST":
        titel=request.form["title"]
        desc=request.form["desc"]
        todo_1=Todo(title=titel,desc=desc)
        
        db.session.add(todo_1)
        db.session.commit()
    alltodo=Todo.query.all()
    return render_template("index.html",alltodo=alltodo)


# ------This query is use to show data in terminal------
@app.route("/show")
def show():
    alltodo=Todo.query.all()
    print(alltodo)
    return "************* This page is use to show all data in TERMINAL **********"

if __name__=="__main__":
    app.run(debug=True)

