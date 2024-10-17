from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return "Welcome to my website"

@app.route('/index', methods=['GET'])
def index():
    return "This is the index page"

#varibale rule
@app.route('/success/<int:score>')
def sucess(score):
    return "Congratulations, you scored "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Person failed'+str(score)

@app.route('/index',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)