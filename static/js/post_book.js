
const input_file1 = document.getElementById("image_1");
const input_file2 = document.getElementById("image_2");
const input_file3 = document.getElementById("image_3");
const input_file4 = document.getElementById("image_4");
const input_file5 = document.getElementById("image_5");
const input_file6 = document.getElementById("image_6");
// const post_image = document.querySelectorAll(".post-img");
const image_group = document.querySelector(".image-group");

image_group.addEventListener("click",function(e){
    // console.log(e.target)
    // e.target.addEventListener("click",function(){
    input_file = e.target.previousElementSibling;
    close_icon = e.target.nextElement;
    if (input_file.id == "image_1"){
        input_file1.click();
        wrapper = input_file1.parentElement;
        show_image(input_file1,wrapper,e.target);
    }
    else if (input_file.id == "image_2"){
        input_file2.click();
        wrapper = input_file2.parentElement;
        show_image(input_file2,wrapper);
    }
    else if (input_file.id == "image_3"){
        input_file3.click();
        wrapper = input_file3.parentElement;
        show_image(input_file3,wrapper);
    }
    else if (input_file.id == "image_4"){
        input_file4.click();
        wrapper = input_file4.parentElement;
        show_image(input_file4,wrapper);
    }
    else if (input_file.id == "image_5"){
        input_file5.click();
        wrapper = input_file5.parentElement;
        show_image(input_file5,wrapper);
    }
    else if (input_file.id == "image_6"){
        input_file6.click();
        wrapper = input_file6.parentElement;
        show_image(input_file6,wrapper);
    }
    else {
        console.log("Something Wrong.....")
    }
    // console.log(input_file1.id)
})

function show_image(input_files,wrapper,upload_icon){
    input_files.addEventListener("change",function (){
        const file = this.files[0];
        // console.log(file)
        if (file){
            const reader = new FileReader();
    
            reader.addEventListener("load",function(){
                wrapper.style.backgroundImage = `url("${this.result}")`;
                upload_icon.style.opacity = 0;
            });
            reader.readAsDataURL(file);
        }
    })
}
