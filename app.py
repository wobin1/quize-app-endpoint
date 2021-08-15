from flask import  Flask, render_template, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:peacedauda@localhost/exam_db'
app.config['SECRET_KEY'] = 'thisisasecret'

db=SQLAlchemy(app)
migrate = Migrate(app, db)

# database models
class Question(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    quest = db.Column(db.String(100), nullable=False)
    optionA = db.Column(db.String(50), nullable=False)
    optionB = db.Column(db.String(50), nullable=False)
    optionC = db.Column(db.String(50), nullable=False)
    ans = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"{self.quest} - {self.optionA} - {self.optionB} - {self.optionC}"


@app.route('/')
#enabling cors
@cross_origin(support_credentials=True)
def index():
    #querying data
    questions = Question.query.all()
    qustions_out = []

    #adding data into the above list
    for question in questions:
        questions_data ={'quest':question.quest, 'optionA':question.optionA, 'optionB':question.optionB, 'optionC':question.optionC, 'ans':question.ans}
        qustions_out.append(questions_data)
    return {"questions":qustions_out}


@app.route('/post_question', methods=["POST"])
def post():
    if request.method=='POST':
        data = json.loads(request.data, strict=False)
        question = Question(quest=data['quest'], optionA=data['optionA'], optionB=data['optionB'], optionC=data['optionC'], ans=data['ans'] )
        db.session.add(question)
        db.session.commit()
        return jsonify({'id': question.id})


@app.route('/delete_question/<id>', methods=['DELETE'])
def question_delete(id):
    question = Question.query.get(id)

    if question is None:
        return {"Error": "not found"}
    else:
        db.session.delete(question)
        db.session.commit()
    return {"message": "question deleted succesfully"}

if __name__ == "__main__":
    app.run(debug=True)