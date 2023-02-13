from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("esercizio1.html") 

@app.route('/immagini')
def immagini():
    return render_template("immagini.html", Titolo='Welcome', Testo='Hello, world!') 

@app.route('/duomo')
def duomo():
  return render_template("duomo.html")

@app.route('/sforzesco')
def sforzesco():
  return render_template("sforzesco.html")

@app.route('/galleria')
def galleria():
  return render_template("galleria.html")

@app.route('/teatro')
def scala():
  return render_template("scala.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  # realizzare un sito web con flask che offra le seguenti funzionalità 
  # 1. La homepage deve fornire una breve descrizione delle caratteristiche della città di Milano
  # 2. Al link <nomesito>/immagini devono essere visualizzate le immagini di 4 monumenti di Milano (controllare sul sito del Prof, come si fa a mettere le immagini)
  # 3. Fare in modo che cliccando sull'immagine si venga mandati ad un breve testo descrittivo del monumento (controllare sul sito del Prof)
  # 4. La repository che conterrà il sito si chiamerà FlaskMilano