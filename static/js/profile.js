// User Profile
// const check_profile = document.getElementById("check_profile");
const user_option = document.querySelector(".user-option");
const body = document.querySelector("body");
const box = document.getElementById("box");
// const account = document.querySelector(".account");

body.addEventListener("click",(e) => {
    console.log(e.target)
    if (e.target.id == "user"){
        user_option.style.display = "block";
    }
    else if(e.target.id == "option"){
        box.style.display = "block";
    }
    else {
        box.style.display = "none";
        user_option.style.display = "none";
    }
})

async function address(){
    const res = await fetch("../../static/js/address.json");
    // const res = await fetch("../../static/js/profile.js");

    const data = await res.json();
    return data;
}

const state = document.getElementById("state");
const city = document.getElementById("city");
const area = document.getElementById("area");
const city_box = document.getElementById("city_box");
const area_box = document.getElementById("area_box");
state_output = "";

address()
    .then((data) => {
        data.state.forEach(function(state){
            state_output += `
                <option value="${state.toLowerCase()}"> ${state} </option>
            `;
        })
        state.innerHTML = state_output;
        // console.log(data.state);
    });

state.addEventListener("change",function(e){
    const state_name = e.target.value;
    // console.log(state_name);
    city_output = "";
    address()
        .then((data) => {
            data[state_name].forEach(function(city){
                city_output += `
                    <option value="${city.toLowerCase()}">${city}</option>
                `;    
            });
            city.innerHTML = city_output;
            city_box.style.display = "block";
            console.log(data[state_name]);
        });
})

city.addEventListener("change",function(e){
    const city_name = e.target.value;
    // console.log(city_name);
    area_output = "";
    address()
        .then((data) => {
            data[city_name].forEach(function(area){
                area_output += `
                    <option value="${area.toLowerCase()}">${area}</option>
                `;  
            });
            area.innerHTML = area_output;
            area_box.style.display = "block";
            console.log(data[city_name]);
        });
})
