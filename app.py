from flask import Flask, render_template, request
import pandas as pd
import trial2

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/problem")
def problem():
    return render_template('problem.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/solution",methods=['POST','GET'])
def csv_upload():
    if(request.method=='GET'):
        return render_template('csv_upload.html')
    else :
        input_df_1 = pd.read_csv(request.files['file1'])
        input_df_2 = pd.read_csv(request.files['file2'])
        input_df_3 = pd.read_csv(request.files['file3'])

        output_df = trial2.main(input_df_1,input_df_2,input_df_3)
        return render_template('output_data.html',output_df=output_df,l=len(output_df))

app.run(debug=True)
