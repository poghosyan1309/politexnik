from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    print("Form submitted!")  # Debug statement

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    dname = request.form['dname']
    feedback = request.form['subject']

    print("Firstname:", firstname)  # Debug statement
    print("Lastname:", lastname)  # Debug statement
    print("Dname:", dname)  # Debug statement
    print("Feedback:", feedback)  # Debug statement

    try:
        file_path = 'feedback.txt'
        print('file path :',file_path)
        with open('feedback.txt', 'a') as file:
            file.write(f"Name: {firstname}\n")
            file.write(f"Lastname: {lastname}\n")
            file.write(f"Dname: {dname}\n")
            file.write(f"Feedback: {feedback}\n\n")
        print("Data saved to file successfully!")
    except Exception as e:
        print("Error occurred while writing to file:", e)

    return render_template('index1.html')


if __name__ == '__main__':
    app.run(debug=True)
