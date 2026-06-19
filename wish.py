from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Best of Luck Sanskruti</title>

<style>
body{
    background: linear-gradient(135deg,#a8edea,#fed6e3);
    font-family: Arial, sans-serif;
    text-align:center;
    padding:50px;
}

.card{
    background:white;
    max-width:700px;
    margin:auto;
    padding:30px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.2);
}

h1{
    color:#6a1b9a;
}

button{
    padding:12px 25px;
    font-size:18px;
    border:none;
    border-radius:10px;
    background:#6a1b9a;
    color:white;
    cursor:pointer;
}

#message{
    margin-top:25px;
    font-size:20px;
    line-height:1.8;
}
</style>
</head>

<body>

<div class="card">

<h1>📚 Special Message</h1>

<p>Click below for a surprise.</p>

<button onclick="showWish()">
Open Surprise 🎁
</button>

<div id="message"></div>

</div>

<script>

function showWish(){

document.getElementById("message").innerHTML = `

<h2>🤔 Wait A Minute...</h2>

<p>

Ek bahut special student ke liye message hai...

<br><br>

Thodi hatti behen 😆<br>
Thodi ziddi 😜<br>
Kabhi kabhi overthinker 🤓<br>

<br>

Par dil ki achhi aur mehnati bhi 💪

<br><br>

Guess who...? 👀

</p>

`;

setTimeout(function(){

document.getElementById("message").innerHTML = `

<h1>🎉 Best Of Luck Sanskruti 🎉</h1>

<p>

📚 Exam ka time aa gaya hai.

Mujhe pata hai ki tum achha karogi.

Bas confidence ke saath paper dena,
aur bilkul tension mat lena.

Tumhari mehnat zaroor rang layegi. ✨

May you achieve great success,
score amazing marks,
and make yourself proud. 🌟

All The Best For Your Exam! 📖

</p>

<h3>🌸 From Monu 🌸</h3>

`;

},3000);

}

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True,port=1245)