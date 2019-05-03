from flask import Flask, render_template, request, url_for, redirect
import requests
import json

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST','GET'])
def hasil():
    namapokemon=request.form['namapokemon']
    namapokemon=namapokemon.lower()
    url1='https://pokeapi.co/api/v2/pokemon/'
    url2='https://pokeapi.co/api/v2/pokemon/'+namapokemon
    data1=requests.get(url1)
    data2=requests.get(url2)

    for i in range (len(data1.json()["results"])):
        if i<len(data1.json()["results"])-1:
            if namapokemon==data1.json()['results'][i]['name']:
                no=data2.json()["id"]
                tinggi=data2.json()["height"]
                berat=data2.json()["weight"]
                return render_template('pokemon.html',y=data2,namapokemon=namapokemon,id=no,berat=berat, tinggi=tinggi)
            else:
                continue
        else:
            if namapokemon==data1.json()['results'][i]['name']:
                no=data2.json()["id"]
                tinggi=data2.json()["height"]
                berat=data2.json()["weight"]
                return render_template('pokemon.html',y=data2,namapokemon=namapokemon,id=no,berat=berat, tinggi=tinggi)
            else:
                return redirect(url_for('error'))


#error handler
@app.errorhandler(404)
def error(x):
    return render_template('error.html')

      

if __name__=='__main__':
    app.run(debug=True)