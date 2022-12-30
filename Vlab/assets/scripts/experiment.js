const intro_and_pro_btn = document.getElementById("intro_and_pro_btn");
const simulation_btn = document.getElementById("simulation_btn");
const observe_btn = document.getElementById("observe_btn");
const result_btn = document.getElementById("result_btn");
const calc_btn = document.getElementById("calc_btn");
const eval_btn = document.getElementById("eval_btn");

intro_and_pro_btn.onclick= function(){
    intro_and_pro_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "block";
    simulation_btn.style.border = "none";
    document.getElementById("simulation").style.display = "none";
    observe_btn.style.border = "none";
    document.getElementById("observe").style.display = "none";
    result_btn.style.border = "none";
    document.getElementById("result").style.display = "none";
    calc_btn.style.border = "none";
    document.getElementById("calc").style.display = "none";
    eval_btn.style.border = "none";
    document.getElementById("eval").style.display = "none";
};

simulation_btn.onclick= function(){
    simulation_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "none";
    intro_and_pro_btn.style.border = "none";
    document.getElementById("simulation").style.display = "block";
    document.getElementById("observe").style.display = "none";
    observe_btn.style.border = "none";
    document.getElementById("result").style.display = "none";
    result_btn.style.border = "none";
    document.getElementById("calc").style.display = "none";
    calc_btn.style.border = "none";
    document.getElementById("eval").style.display = "none";
    eval_btn.style.border = "none";
};
observe_btn.onclick= function(){
    observe_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "none";
    intro_and_pro_btn.style.border = "none";
    document.getElementById("simulation").style.display = "none";
    simulation_btn.style.border = "none";
    document.getElementById("observe").style.display = "block";
    document.getElementById("result").style.display = "none";
    result_btn.style.border = "none";
    document.getElementById("calc").style.display = "none";
    calc_btn.style.border = "none";
    document.getElementById("eval").style.display = "none";
    eval_btn.style.border = "none";
};
result_btn.onclick= function(){
    result_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "none";
    intro_and_pro_btn.style.border = "none";
    document.getElementById("simulation").style.display = "none";
    simulation_btn.style.border = "none";
    document.getElementById("observe").style.display = "none";
    observe_btn.style.border = "none";
    document.getElementById("result").style.display = "block";
    document.getElementById("calc").style.display = "none";
    calc_btn.style.border = "none";
    document.getElementById("eval").style.display = "none";
    eval_btn.style.border = "none";
};
calc_btn.onclick= function(){
    calc_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "none";
    intro_and_pro_btn.style.border = "none";
    document.getElementById("simulation").style.display = "none";
    simulation_btn.style.border = "none";
    document.getElementById("observe").style.display = "none";
    observe_btn.style.border = "none";
    document.getElementById("result").style.display = "none";
    result_btn.style.border = "none";
    document.getElementById("calc").style.display = "block";
    document.getElementById("eval").style.display = "none";
    eval_btn.style.border = "none";
};

eval_btn.onclick= function(){
    eval_btn.style.border = "1px solid #fff";
    document.getElementById("intro_and_pro").style.display = "none";
    intro_and_pro_btn.style.border = "none";
    document.getElementById("simulation").style.display = "none";
    simulation_btn.style.border = "none";
    document.getElementById("observe").style.display = "none";
    observe_btn.style.border = "none";
    document.getElementById("result").style.display = "none";
    result_btn.style.border = "none";
    document.getElementById("calc").style.display = "none";
    calc_btn.style.border = "none";
    document.getElementById("eval").style.display = "block";
};