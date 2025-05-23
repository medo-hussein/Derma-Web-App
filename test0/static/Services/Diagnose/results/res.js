document.getElementById("result-one").addEventListener("click", function() {
    document.getElementsByClassName("popup-res1")[0].classList.add("active");
});

document.getElementById("ok-btn1").addEventListener("click", function() {
    document.getElementsByClassName("popup-res1")[0].classList.remove("active");
});


document.getElementById("result-two").addEventListener("click", function() {
    document.getElementsByClassName("popup-res2")[0].classList.add("active");
});

document.getElementById("ok-btn2").addEventListener("click", function() {
    document.getElementsByClassName("popup-res2")[0].classList.remove("active");
});


document.getElementById("result-three").addEventListener("click", function() {
    document.getElementsByClassName("popup-res3")[0].classList.add("active");
});

document.getElementById("ok-btn3").addEventListener("click", function() {
    document.getElementsByClassName("popup-res3")[0].classList.remove("active");
});


document.getElementById("result-four").addEventListener("click", function() {
    document.getElementsByClassName("popup-res4")[0].classList.add("active");
});

document.getElementById("ok-btn4").addEventListener("click", function() {
    document.getElementsByClassName("popup-res4")[0].classList.remove("active");
});
// /////////////////////////////////////////////////////////////////////////////////////
doc1=document.currentScript.dataset;
var var1=JSON.parse( doc1['username'])["m"]["data"];
// /////////////////////////////////////////////////////////////////////////////////////
console.log(typeof var1[0]["probability"])
let percentage1 = document.getElementById("percentage1");
let counter1 = 0;
setInterval(() => {
    if (counter1 === var1[0]["probability"] ) {
        clearInterval();
    } else {
        counter1 += 1;
        percentage1.innerHTML = counter1 + "%";
    }
}, 10);

let percentage2 = document.getElementById("percentage2");
let counter2 = 0;
setInterval(() => {
    if (counter2 == var1[1]["probability"] ) {
        clearInterval();
    } else {
        counter2 += 1;
        percentage2.innerHTML = counter2 + "%";
    }
}, 10);

let percentage3 = document.getElementById("percentage3");
let counter3 = 0;
setInterval(() => {
    if (counter3 == var1[2]["probability"] ) {
        clearInterval();
    } else {
        counter3 += 1;
        percentage3.innerHTML = counter3 + "%";
    }
}, 10);

let percentage4 = document.getElementById("percentage4");
let counter4 = 0;
setInterval(() => {
    if (counter4 == var1[3]["probability"] ) {
        clearInterval();
    } else {
        counter4 += 1;
        percentage4.innerHTML = counter4 + "%";
    }
}, 10);
var d_name12 =var1[0]["class_name"]
var d_name1 = document.getElementById("d_name1");
d_name1.innerHTML=d_name12;

d_name1 = document.getElementById("name1");
d_name1.innerHTML=d_name12;

d_name12 =var1[1]["class_name"]
d_name1 = document.getElementById("d_name2");
d_name1.innerHTML=d_name12;

d_name1 = document.getElementById("name2");
d_name1.innerHTML=d_name12;

d_name12 =var1[2]["class_name"]
d_name1 = document.getElementById("d_name3");
d_name1.innerHTML=d_name12;

d_name1 = document.getElementById("name3");
d_name1.innerHTML=d_name12;

d_name12 =var1[3]["class_name"]
d_name1 = document.getElementById("d_name4");
d_name1.innerHTML=d_name12;

d_name1 = document.getElementById("name4");
d_name1.innerHTML=d_name12;
