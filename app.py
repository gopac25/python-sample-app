"""
Sample flask app for deploying classifier model
Using Jenkins & Github Actions
ECS,EKS,AKS
"""
import pickle
import random
from flask import Flask, request, render_template

app = Flask(__name__)

with open("./artefacts/classifier.pkl", "rb") as model_pickle:
    clf = pickle.load(model_pickle)
# model_pickle = open("./classifier.pkl", "rb")


# list of cat images
images = ["aai1.jpeg","aai2.jpeg",]

@app.route('/')
def index():
    """
    Main page
    """
    url = random.choice(images)
    return render_template('index.html', url=url)

@app.route("/ping", methods=['GET'])
def ping():
    """
    Check working status
    """
    return {"message": "Hi there, I'm working with the new API!!"}


@app.route("/params", methods=['GET'])
def get_application_params():
    """
    Input parameters
    """
    parameters = {
    'Gender': "<Male/Female>",
    'Married': "<Married/Unmarried>",
    'ApplicantIncome': "<Income amount>",
    'Credit_History': "Cleared Debts",
    'LoanAmount': "<Loan Amount>"
    }
    return parameters


##defining the endpoint which will make the prediction
@app.route("/predict", methods=['POST'])
def prediction():
    """
    Returns loan application status using ML model
    """
    loan_req = request.get_json()
    print(loan_req)

    if loan_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1
    if loan_req['Married'] == "Unmarried":
        married = 0
    else:
        married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        credit_history = 0
    else:
        credit_history = 1
    applicant_income = loan_req['ApplicantIncome']
    loan_amount = loan_req['LoanAmount']

    result = clf.predict([[gender, married, applicant_income, loan_amount, credit_history]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
    return {"loan_approval_status": pred}

if __name__ == '__main__':
    app.run()
