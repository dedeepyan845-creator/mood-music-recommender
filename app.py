from flask import Flask, render_template_string, request

app = Flask(__name__)

# KEEP YOUR SAME songs = { ... } HERE
songs = {
    "happy": [
        {"name": "Good Time", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
        {"name": "Can't Stop The Feeling", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
        {"name": "Uptown Funk", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
        {"name": "Shake It Off", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"},
        {"name": "Best Day Of My Life", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"},
        {"name": "Roar", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"},
        {"name": "Firework", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"},
        {"name": "Sugar", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"},
        {"name": "On Top Of The World", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"}
    ],

    "sad": [
        {"name": "Someone Like You", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"},
        {"name": "Let Her Go", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"},
        {"name": "Stay With Me", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"},
        {"name": "Fix You", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"},
        {"name": "Photograph", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"},
        {"name": "Memories", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
        {"name": "All I Want", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
        {"name": "Happier", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
        {"name": "Say Something", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
        {"name": "When I Was Your Man", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"}
    ],

    "angry": [
        {"name": "Believer", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"},
        {"name": "Enemy", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"},
        {"name": "Stronger", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"},
        {"name": "Numb", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"},
        {"name": "Thunder", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"},
        {"name": "Warriors", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"},
        {"name": "Remember The Name", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"},
        {"name": "Centuries", "url": "https://www.soundHelix.com/examples/mp3/SoundHelix-Song-13.mp3"},
        {"name": "Fight Song", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"},
        {"name": "Whatever It Takes", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"}
    ],

    "relaxed": [
        {"name": "Perfect", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
        {"name": "Memories", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
        {"name": "Photograph", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
        {"name": "Senorita", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
        {"name": "Lovely", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"},
        {"name": "Night Changes", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"},
        {"name": "Peaches", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"},
        {"name": "Calm Down", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"},
        {"name": "Perfect Strangers", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3"},
        {"name": "Shape Of You", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"}
    ],

    "motivated": [
        {"name": "Hall Of Fame", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-11.mp3"},
        {"name": "Unstoppable", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-12.mp3"},
        {"name": "Rise Up", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-13.mp3"},
        {"name": "Stronger", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-14.mp3"},
        {"name": "Champion", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-15.mp3"},
        {"name": "On My Way", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
        {"name": "Legends Never Die", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
        {"name": "The Greatest", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
        {"name": "Never Give Up", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
        {"name": "Power", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"}
    ]
}   
    

html = """
<!DOCTYPE html>
<html>
<head>
<title>Mood Music Player</title>

<style>
body{
    margin:0;
    font-family:Arial, sans-serif;
    text-align:center;
    min-height:100vh;
    background-color:#ffd6e7;

    background-image:
        radial-gradient(#ffffff90 2px, transparent 2px),
        radial-gradient(#ffc2da 2px, transparent 2px);

    background-size:40px 40px;
    background-position:0 0, 20px 20px;

    display:flex;
    justify-content:center;
    align-items:center;
}

.box{
    background:rgba(255,255,255,0.9);
    width:500px;
    padding:30px;
    border-radius:25px;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
}

h1{
    color:#d85b8f;
}

select, button{
    padding:10px 14px;
    margin:8px;
    border:none;
    border-radius:12px;
    font-size:16px;
}

select{
    background:#fff5f9;
}

button{
    background:#f48fb1;
    color:white;
    cursor:pointer;
}

button:hover{
    background:#ec7ea5;
}

h3{
    color:#c94f82;
}
</style>
</head>

<body>

<div class="box">

<h1>Mood Music Player 🎀🎵</h1>

<form method="POST">
<select name="mood">
<option value="happy">Happy 😊</option>
<option value="sad">Sad 😔</option>
<option value="angry">Angry 😡</option>
<option value="relaxed">Relaxed 😌</option>
<option value="motivated">Motivated 💪</option>
</select>

<button type="submit" name="action" value="show">Show Songs</button>
</form>

{% if song_list %}
<form method="POST">
<input type="hidden" name="mood" value="{{ mood }}">

<select name="song_index">
{% for s in song_list %}
<option value="{{ loop.index0 }}">{{ s['name'] }}</option>
{% endfor %}
</select>

<button type="submit" name="action" value="play">Play Selected</button>
</form>
{% endif %}

{% if song %}
<h3>{{ song['name'] }}</h3>

<audio controls autoplay>
<source src="{{ song['url'] }}" type="audio/mpeg">
</audio>
{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    song = None
    song_list = None
    mood = "happy"

    if request.method == "POST":
        mood = request.form["mood"]
        song_list = songs[mood]

        if request.form["action"] == "play":
            index = int(request.form["song_index"])
            song = songs[mood][index]

    return render_template_string(
        html,
        song=song,
        song_list=song_list,
        mood=mood
    )
if __name__ == "__main__":
    app.run()