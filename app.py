from flask import Flask,request,render_template


#app=Flask(__name__)
obj=Flask(__name__)


#@app.route('/')
@obj.route('/')
def welcome():
    return "<h1>Hi welcome again to flask</h1>"

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="division":
        result=number1/number2
    else:
        result=number1-number2
    return result

print(__name__)


if __name__=='__main__':  #to run the file in stand alone mode
    obj.run()
    #app.run(debug=True)