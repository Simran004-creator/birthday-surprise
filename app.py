
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Happy Birthday HUSAN</title>

<style>

body{
    margin:0;
    padding:0;
    overflow-x:hidden;
    overflow-y:auto;
    min-height:100vh;
    font-family:'Comic Sans MS', cursive;
    text-align:center;

    background:linear-gradient(
    135deg,
    #0b1026,
    #111827,
    #1e1b4b,
    #312e81
    );
}

::-webkit-scrollbar{
    width:12px;
}

::-webkit-scrollbar-track{
    background:#ffd1dc;
}

::-webkit-scrollbar-thumb{
    background:#ff69b4;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#ff1493;
}

.container{
     margin-top:20px;
    padding-bottom:200px;
}

h1{
    color:white;
    font-size:60px;
    text-shadow:0 0 15px hotpink;
    animation:glow 2s infinite alternate;
}
.star{
    position:absolute;
    color:white;
    font-size:25px;
    animation:twinkle 2s infinite alternate;
}

@keyframes twinkle{
    from{
        opacity:0.3;
    }
    to{
        opacity:1;
        text-shadow:0 0 15px white;
    }
}
.message{
    color:white;
    font-size:28px;
    margin-top:-10px;
}

.characters{
    display:flex;
    justify-content:center;
    align-items:center;
    gap:40px;
    margin-top:20px;
    position:relative;
    animation:walk 12s linear infinite;
}
.sparkle{
    position:absolute;
    font-size:30px;
    animation:sparkle 5s linear infinite;
}

@keyframes sparkle{
    0%{
        transform:translateY(100vh) rotate(0deg);
        opacity:0;
    }
    50%{
        opacity:1;
    }
    100%{
        transform:translateY(-120vh) rotate(360deg);
        opacity:0;
    }
}

@keyframes walk{
    0%{
        transform:translateX(-300px);
    }
    100%{
        transform:translateX(300px);
    }
}

.dudu{
    font-size:180px;
    animation:bounce 2s infinite;
}

.bubu{
    font-size:180px;
    animation:bounce 2s infinite 1s;
}

.cake{
    font-size:120px;
    animation:float 3s infinite;
}

button{
    margin-top:20px;
    padding:18px 35px;
    font-size:24px;
    border:none;
    border-radius:50px;
    background:#ff69b4;
    color:white;
    cursor:pointer;
    box-shadow:0 0 15px pink;
    transition:0.3s;
}

button:hover{
    transform:scale(1.1);
    background:#ff1493;
}

.balloon{
    position:absolute;
    bottom:-150px;
    font-size:55px;
    animation:rise 12s linear infinite;
}

.heart{
    position:absolute;
    color:pink;
    font-size:30px;
    animation:hearts 6s linear infinite;
}

#loveLetter{
    position:relative;
    z-index:999;
}

@keyframes bounce{
    0%,100%{
        transform:translateY(0);
    }
    50%{
        transform:translateY(-30px);
    }
}

@keyframes float{
    0%,100%{
        transform:translateY(0);
    }
    50%{
        transform:translateY(-18px);
    }
}

@keyframes glow{
    from{
        text-shadow:0 0 10px white;
    }
    to{
        text-shadow:0 0 30px yellow;
    }
}

@keyframes rise{
    0%{
        transform:translateY(0);
    }
    100%{
        transform:translateY(-130vh);
    }
}

@keyframes hearts{
    0%{
        transform:translateY(100vh) scale(0.5);
        opacity:1;
    }
    100%{
        transform:translateY(-100vh) scale(1.5);
        opacity:0;
    }
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
} 

@media(max-width:768px){

    h1{
        font-size:40px;
    }

    .message{
        font-size:20px;
        padding:0 10px;
    }

    .dudu,.bubu{
        font-size:110px;
    }

    .cake{
        font-size:70px;
    }

    button{
        font-size:18px;
        padding:14px 25px;
    }
}

.moon{
    position:absolute;
    top:30px;
    right:40px;
    font-size:80px;
    filter:drop-shadow(0 0 20px white);
}

.shooting-star{
    position:absolute;
    color:white;
    font-size:20px;
    animation:shoot 6s linear infinite;
}

@keyframes shoot{
    0%{
        transform:translate(-100px,-100px);
        opacity:1;
    }
    100%{
        transform:translate(120vw,120vh);
        opacity:0;
    }
}

#envelope{
    display:none;
    font-size:120px;
    cursor:pointer;
    margin-top:30px;
    transition:0.4s;
    animation:bounce 2s infinite;
}

#envelope:hover{
    transform:scale(1.15);
}

.letter{
    display:none;
    width:85%;
    max-width:700px;
    margin:30px auto;
    background:rgba(15,15,40,0.95);
    color:white;
    padding:30px;
    border-radius:25px;
    box-shadow:0 0 30px hotpink;
    border:4px solid #ff69b4;
    font-size:22px;
    line-height:1.8;
    animation:fadeIn 1s ease;
}

</style>
</head>

<body>

<div class="container">

<h1>🎉 Happy Birthday HUSAN 🎉</h1>
<h2 id="clock" style="color:white;"></h2>
<div class="message">
Dudu & Bubu Came To Celebrate Your Special Day 💖
</div>


<div class="characters">

<div class="dudu">🐻</div>

<div class="cake">🎂</div>

<div class="bubu">🐼</div>

</div>

<button id="wishBtn">
Click Dudu & Bubu 💕
</button>

<div style="margin-top:30px;">

    <img id="photo"
         src="/static/1.jpeg"
         width="500"
         style="
         border-radius:25px;
         box-shadow:0 0 25px hotpink;
         transition:opacity .5s ease;
         max-width:90%;
         border:5px solid white;
         ">

</div>

<div id="gift"
     style="font-size:90px;cursor:pointer;margin-top:20px;">
🎁
</div>

<div id="giftMessage"
     style="display:none;color:white;font-size:28px;">
💖 Surprise! Dudu & Bubu Love You Forever! 💖
</div>

<div id="envelope">
    💌
</div>

<div id="loveLetter" class="letter">

    <h2>💖 A Special Letter 💖</h2>

    <p>
    Happy Birthday HUSAN ❤️

    <br><br>

    You are the reason behind so many of my smiles.

    Thank you for being such a wonderful person and for making life more beautiful every day.

    May your birthday be filled with love, happiness, laughter and all your favorite things. 🎂✨

    You deserve all the joy in the world today and always.

    <br><br>

    I Love You Forever 💖

    <br><br>

    🐼 Your Bubu 🐼
    </p>

</div>

<div class="star" style="top:5%;left:10%;">⭐</div>
<div class="star" style="top:15%;left:80%;">⭐</div>
<div class="star" style="top:30%;left:20%;">✨</div>
<div class="star" style="top:40%;left:90%;">⭐</div>
<div class="star" style="top:60%;left:15%;">✨</div>
<div class="star" style="top:75%;left:70%;">⭐</div>
<div class="star" style="top:90%;left:40%;">✨</div>

<!-- Balloons -->

<div class="balloon" style="left:5%">🎈</div>
<div class="balloon" style="left:20%;animation-delay:2s;">🎈</div>
<div class="balloon" style="left:40%;animation-delay:4s;">🎈</div>
<div class="balloon" style="left:60%;animation-delay:1s;">🎈</div>
<div class="balloon" style="left:80%;animation-delay:3s;">🎈</div>

<!-- Hearts -->

<div class="heart" style="left:10%">💖</div>
<div class="heart" style="left:30%;animation-delay:2s;">💖</div>
<div class="heart" style="left:50%;animation-delay:4s;">💖</div>
<div class="heart" style="left:70%;animation-delay:1s;">💖</div>
<div class="heart" style="left:90%;animation-delay:3s;">💖</div>

<div class="moon">🌙</div>
<div class="shooting-star">⭐</div>

<script>

document.addEventListener("DOMContentLoaded", function(){

    const btn = document.getElementById("wishBtn");

    let availableVoices = [];

    function loadVoices(){
        availableVoices = speechSynthesis.getVoices();
    }

    loadVoices();

    if(speechSynthesis.onvoiceschanged !== undefined){
        speechSynthesis.onvoiceschanged = loadVoices;
    }

    btn.addEventListener("click", function(){

        speechSynthesis.cancel();

        const voiceMessage = new SpeechSynthesisUtterance(
            "Happy Birthday HUSAN! Dudu and Bubu brought cake, hugs, love and lots of happiness for you! May your smile always shine bright! Your Bubu is always there for you and loves you so much!"
        );

        voiceMessage.pitch = 1.3;
        voiceMessage.rate = 0.95;
        voiceMessage.volume = 1;

        const femaleVoice =
            availableVoices.find(v => v.name.includes("Zira")) ||
            availableVoices.find(v => v.name.includes("Samantha")) ||
            availableVoices.find(v => v.name.includes("Google UK English Female")) ||
            availableVoices.find(v => v.name.toLowerCase().includes("female"));

        if(femaleVoice){
            voiceMessage.voice = femaleVoice;
        }

        speechSynthesis.speak(voiceMessage);

        confetti({
            particleCount:250,
            spread:120,
            origin:{y:0.6}
        });
          
       document.getElementById("envelope").style.display = "block";

        setTimeout(function(){
            alert("🐻🐼 Dudu & Bubu Love You 💖");
        },1000);

    });


    const photos = [
    "/static/1.jpeg",
    "/static/2.jpeg",
    "/static/3.jpeg"
];

    let currentPhoto = 0;

    setInterval(function(){

        currentPhoto++;

        if(currentPhoto >= photos.length){
            currentPhoto = 0;
        }

        document.getElementById("photo").src =
            photos[currentPhoto];

    },3000);

    setInterval(function(){

    confetti({
        particleCount:100,
        spread:80,
        origin:{
            x:Math.random(),
            y:Math.random()*0.5
        }
    });

},5000);
 
function updateClock(){
    document.getElementById("clock").innerHTML =
        "🕒 " + new Date().toLocaleTimeString();
}

setInterval(updateClock,1000);
updateClock();

const photo = document.getElementById("photo");

photo.style.opacity = "0";

setTimeout(() => {
    photo.src = photos[currentPhoto];
    photo.style.opacity = "1";
}, 400);

    document.getElementById("gift").onclick = function(){

        this.innerHTML = "💝";

        document.getElementById("giftMessage").style.display =
            "block";

        confetti({
            particleCount:150,
            spread:100
        });

    };

    document.getElementById("envelope").onclick = function(){

    this.innerHTML = "💖";

    document.getElementById("loveLetter").style.display = "block";

    confetti({
        particleCount:200,
        spread:120
    });

};

});

</script>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

<div style="
margin-top:80px;
padding:30px;
font-size:26px;
color:white;
text-shadow:0 0 10px hotpink;
">

💖 Made With Love By Bubu for Dudu 💖

<br><br>

🐻 ❤️ 🐼

</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)


