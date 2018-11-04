from flask import Flask
from flask import redirect,request,url_for,render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def coming_soon():

	if request.method == "POST":
		disable = 'disabled'
		email = request.form.get('email')
		with open ('signup.txt', 'a') as f:
			f.write(email+"\n")
		return render_template('index.html', disable=disable)
	else:
		disable = ''
    	return render_template('index.html', disable=disable)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
