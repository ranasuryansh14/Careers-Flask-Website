from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'SPOC',
    'location': 'DSW-CGC',
    'salary': 'Rs. 1000'
  },
  {
    'id': 2,
    'title': 'President',
    'location': 'DSW',
    'salary': 'Rs. 1000'
  },
  {
    'id': 3,
    'title': 'President',
    'location': 'DSW-CLUBS'
  },
  {
    'id': 4,
    'title': 'Vice President',
    'location': 'DSW-CLUBS'
  }
]

@app.route("/")
def hello_rana():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='CGC - DSW')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)