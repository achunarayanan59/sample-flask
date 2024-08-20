from flask import Flask , render_template,request

app=Flask(__name__)

@app.route('/')
def home():
        name=request.args.get('name','hello')
        fname=request.args.get('fname','invalid')
        lname=request.args.get('lname','invalid')
        return render_template('index.html',placeholder=name,fname=fname,lname=lname)


if __name__=='__main__':
    app.run(debug=True)
