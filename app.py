from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy database of Tamil songs
lyrics_db = {
    "vaathi coming": "Haan, Han Han Han Han, Hak Han Hak Han, Ei Enna Da Idhu, Sappa Beatu Koluthungada, Aah Maja Pa Maja Pa, Idhan Idhan Idhan Idhan, Ei Idi Da Vanga Da, Eh Vathi Coming Oththu, Ah Ah, Ei Oththu, Dhakka Dhunna, Dompa Dompa, Hoi, Anna Vandha Atom Bombu, Dummu, Pilu Pilu Pilu Pillami, Pilu Pilu Pilu Aai, Pilu Pilu Pilu Pillami, Pilu Pilu Pilu Eeey, Pilu Pilu Pilu Pilammi, Pilu Pilu Pilu Pilammi, Pilu Pilu Pilu Pilu Pilu Pilu, Vathi Coming Oththu, Oorragara Katte, Ei Tarukkula Triple-U Vutta, Salipila S... - Full article: Vathi Coming Lyrics - Master (Film) | Thalapathy Vijay",
    "enadi mayavi": "Hey, en thalaikkaerura pon thadam podura, En uyiraadura ennadi maayaavi nee, En nelam maaththura andharamaakkura, En nejam kaattura, Pattaa kaththi thookki, Ippa mittai narukkura, Vittaa nenja vaari, Un pattaa kirukkura, Hey, en thalaikkaerura pon thadam podura, En uyiraadura ennadi maayaavi nee, En nelam maaththura andharamaakkura, En nejam kaattura, Vandaa suththum kaaththu, Enna rendaa odaikkudhae, Summaa ninna kaadhal, Ulla nandaa tholaikkudhae, Dhinam kotti theekkavaa oru muttaal megamaa, Unna suththi vaazhavaa un kottaa kaagamaa, Paraivayae parandhu povomaa, maranamae marandhu povomaa, Uppu kaaththula idhu panneer kaalamaa.",
    "rowdy baby": "Hey en goli sodavae, En kari kozhambae, Un kutty puppy naan, Take me, Take me, Hey en silku satta, Nee weightu katta, Loveu sotta sotta, Talk me, Talk me, Hey my dear machaan, Nee manasu vechaa, Namma orasikkalaam, Nenju jigu jigu jaa.",
    "why this kolaveri": "Yo Boys.. I am Singing Song.. Soup Song.. Flop Song.. Why This Kolaveri Kolaveri Kolaveri Dee? Why This Kolaveri Kolaveri Kolaveri Dee? Rhythm Correct.. Why This Kolaveri Kolaveri Kolaveri Dee? Maintain please.. Why This Kolaveri? Adee.. ahhh...Distance'la Moon'nu Moon'nu Moon'nu Color'ru White'tu White'tu Background Night'tu Night'tu Night'tu Color'ru Black'ku Why This Kolaveri Kolaveri Kolaveri Dee? Why This Kolaveri Kolaveri Kolaveri Dee? White'tu Skin'nu Girl'lu Girl'lu Girl'lu Heart'tu Black'ku Eyes'su Eyes'su Meet'tu Meet'tu paiyan Future Dark'ku.. Why This Kolaveri Kolaveri Kolaveri Dee? Why This Kolaveri Kolaveri Kolaveri Dee?",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_lyrics', methods=['POST'])
def get_lyrics():
    user_input = request.json['message'].strip().lower()
    response = lyrics_db.get(user_input, "Sorry, lyrics not found for that song.")
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)
