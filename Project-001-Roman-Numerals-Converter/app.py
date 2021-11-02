from flask import Flask, render_template, request

app = Flask(__name__)


number_dict = {1 : 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',90: 'XC', 100: 'C', 400:'CD',  500: 'D', 900: 'CM', 1000: 'M'}
order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
result = []

def input(number):
  result1 =""
  for x in order:
    if number !=0:
        quotient = number//x
        if quotient !=0:
            for y in range(quotient):
                result1 = result1 + (number_dict[x])
        number = number%x
  return result1


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods =['GET','POST'])
def result():
    if request.method =="POST":
        num = request.form.get("number")
        return render_template ('result.html', number_decimal=num, number_roman=input(int(num)), developer_name="Kamshat Maidan")
    else:
        return render_template("result.html", developer_name="Kamshat Maidan")


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
   