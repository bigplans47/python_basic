from flask import Flask, render_template
# so we import class Flask and function render_template

app = Flask(__name__)
# here a new instance of the flask class is created

@app.route('/')
def home():
    # mapped url / to the function home so if visit '/' url home will execute
    # render_template used to render home.html template
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    # we use run to run app on a local server and set debug flag to view applicable error messages and to auto reload server after changes to the code
    app.run(debug=True)
