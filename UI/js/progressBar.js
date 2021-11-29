const progress = document.getElementById("progress");
const prev = document.getElementById("prev");
// let next = document.getElementById("next");
// let next = document.getElementById('next')
const circles = document.querySelectorAll(".circle");
let headingSection = document.getElementById("headingSection");
let iconSection = document.getElementById("iconSection");
let buttonsSection = document.getElementById("buttonsSection");
let pageTop = document.getElementById("page-top");
let hiddenNext = 0
let currentActive = 1;

let count = 1
console.log(count)

function btnClick(){
    hiddenNext = parseInt(document.getElementById('hiddenNext').value)
    currentActive++;
    document.getElementById('hiddenNext')
    if (currentActive > circles.length) {
        currentActive = circles.length;
    }
    update(hiddenNext);
}

prev.addEventListener("click", () => {
    currentActive--;

    if (currentActive < 1) {
        currentActive = 1;
    }
    update();
});

let headingCount = 0
let imageCount = 0
function update(val) {

    count+=1
    val+=1
    console.log(val)
    buttonsSection.innerHTML = '<button class="btn btn-primary" id="next'+val+'" onclick="btnClick()">Next</button>'
    document.getElementById('hiddenNext').value = val
    let headingList = ['Image Enhancement', 'Abnormal Behaviour Detection', 'Face Detection & Recognition', 'Figure Recognition', 'Scanning Process Successful']
    let iconList = ['./assets/ImageEnhancement.png', './assets/gun_new.png', './assets/FaceDetection&Recognition.png', './assets/FigureRecognition.png']
    headingCount++
    imageCount++
    circles.forEach((circle, idx) => {

        if (idx < currentActive) {

            circle.classList.add("active");
            let heading = headingList[headingCount]
            let image = iconList[imageCount]
            headingSection.innerHTML = '<h4 style="text-align: center; color: white;font-size: 30px" id="function1" class="mx-auto my-0 text-uppercase">'+heading+'</h4>'

            if(iconList.length == imageCount){
                iconSection.innerHTML = '<div class="success-checkmark">\n' +
            '  <div class="check-icon">\n' +
            '    <span class="icon-line line-tip"></span>\n' +
            '    <span class="icon-line line-long"></span>\n' +
            '    <div class="icon-circle"></div>\n' +
            '    <div class="icon-fix"></div>\n' +
            '  </div>\n' +
            '</div>\n'
            } else {
                iconSection.innerHTML = '<img src="'+image+'" style="height: 200px;width: 200px;"/>'
            }

        } else {
            circle.classList.remove("active");
        }
    });

    const actives = document.querySelectorAll(".active");

    progress.style.width = ((actives.length - 1) / (circles.length - 1)) * 100 + "%";

    if (currentActive === 1) {

        prev.disabled = true;

    } else if (currentActive === circles.length) {

          buttonsSection.innerHTML =
            '<a class="btn btn-primary" id="result" href="./results.html"">View Result</a>'

    } else {


        prev.disabled = false;
        document.getElementById('next'+val).disabled = false;
    }
}

