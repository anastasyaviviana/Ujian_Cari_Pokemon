from flask import redirect, request, Flask, render_template, url_for
import json, requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST','GET'])
def post():
    nama=request.form['namapokemon']
    nama=nama.lower()
    url='https://pokeapi.co/api/v2/pokemon/'+nama
    data=requests.get(url)
    if str(data)=='<Response [404]>':
        return redirect(url_for('notfound'))
    nama=data.json()['forms'][0]['name']
    gambar=data.json()['sprites']['front_default']
    id=data.json()['id']
    berat=data.json()['weight']
    tinggi=data.json()['height']
    return render_template('pokemon.html',nama=nama,gambar=gambar,id=id,berat=berat,tinggi=tinggi)

@app.route('/notFound')
def notfound():
    return render_template('error.html')

@app.errorhandler(404)
def notFound404(x):
    return render_template('error.html')

if __name__=='__main__':
    app.run(debug=True)