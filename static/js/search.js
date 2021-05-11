
const search_location = document.getElementById("location");
const form = document.getElementById("search");
search_location.addEventListener("change",(e) => {
    console.log(search_location.value);
    form.submit();
    e.preventDefault();
})