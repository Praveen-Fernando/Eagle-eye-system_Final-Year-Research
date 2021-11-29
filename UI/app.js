const path = document.getElementById('upload')
const submitBtn = document.getElementById('submitBtn')
const submitBtnAbnormal = document.getElementById('submitButton')
const submitBtnFace = document.getElementById('submitBtnFace')
const submitButtonFigure = document.getElementById('submitButtonFigure')



const nextBen4 = document.getElementById('next4')
const mainSubmitBtn = document.getElementById('mainSubmitBtn')
const progressBarSection = document.getElementById('progressBarSection')
let result = document.getElementById('result')
let dataSection = document.getElementById('dataSection')
let datas

if(result != null){
    result.addEventListener('click', (e) => {
    e.preventDefault()

    fetch('http://127.0.0.1:5000/GetAllData', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(resp => resp.json())
        .then((data) => {
            console.log(data)

            dataSection.innerHTML = `<div class="content" id="content1">

                <div>
                    <!-- <p>Your account details are below:</p> -->
                    <table >
                        <tr >
                            <td>Contrast Adjustment : Clahe</td>
                        </tr>
                        <tr>
                            <td>Improve Image Shapness : Unsharp masking</td>
                        </tr>
                        <tr>
                            <td>Noise Type : Gaussian noise</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="content" id="content2">
                <div>
                    <!-- <p>Your account details are below:</p> -->
                    <table >
                        <tr >
                            <td >Incident Type : ${data[0].incident_type}</td>
                        </tr>
                        <tr>
                            <td>Used Weapon Type : ${data[0].used_weapon}  </td>
                        </tr>
                        <tr>
                            <td>Detected Time : ${data[0].detected_time}</td>
                        </tr>

                    </table>
                </div>
            </div>
            <div class="content" id="content3">
                <div>
                    <!-- <p>Your account details are below:</p> -->
                    <table >
                        <tr>
                            <td>Name : ${data[1].Name}</td>
                        </tr>
                        <tr>
                            <td>Date Of Birth : ${data[1].DOB}</td>
                        </tr>
                        <tr>
                            <td>Address : ${data[1].Address}</td>
                        </tr>
                        <tr>
                            <td>Blood Group : ${data[1].Blood_Group}</td>
                        </tr>
                        <tr>
                            <td>NIC : ${data[1].NIC}</td>
                        </tr>
                        <tr>
                            <td>Crimes : ${data[1].Crimes}</td>
                        </tr>
                    </table>
                </div>

            </div>
            <div class="content" id="content4">
                <div>
                    <!-- <p>Your account details are below:</p> -->
                    <table>
                        <tr>
                            <td>Age Range : ${data[2].age}</td>
                        </tr>
                        <tr>
                            <td>Gender : ${data[2].gender}</td>
                        </tr>
                        <tr>
                            <td>Height Range : ${data[2].height}</td>
                        </tr>
                    </table>
                </div>
            </div>`

        })
        .catch(error => console.log('error'))
})
}


//For Image enhancement
function insertVideo(newVideo) {
    displayAlert("Image enhancement started");
    fetch('http://127.0.0.1:5000/StartImageEnhance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newVideo)
    })
        .then(resp => resp.json())
        .then((VidData) => {

            console.log(VidData)
            datas = VidData.id

            if(VidData != null){
                displayAlert("Image enhancement is successfully executed");
                const nextBen1 = document.getElementById('next1')
                nextBen1.addEventListener("click", () => {
                    displayAlert("Abnormal behaviour detection started");
                startAbnormalBehaviourDetection(datas)
                    VidData = null
            })
            }

        })
        .catch(error => console.log('error'))
}

function startAbnormalBehaviourDetection(id) {

    fetch(`http://127.0.0.1:5000/getEnhancedVideo/${id}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(resp => resp.json())
        .then(list => {
            console.log(list)
            fetch(`http://127.0.0.1:5000/startAbnormalBehaviourDetection`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(list)
            })
                .then(resp => resp.json())
                .then(data => {
                    console.log(data)

                    displayAlert("Abnormal behaviour detection is successfully executed");
                    if (data != null) {
                        const nextBen2 = document.getElementById('next2')
                    nextBen2.addEventListener("click", () => {
                        displayAlert("Face detection started");
                        startFaceRecognition();
                        data = null
                    })
                    }
                })
        })
}

function startFaceRecognition() {
    fetch(`http://127.0.0.1:5000/StartFaceRecognition`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(resp => resp.json())
        .then(list => {
            console.log(list)
                // 'E:\\BACKBONE\\face_detection_recognition\\output\\Output_Video.avi'
            displayAlert("Face recognition & identification is successfully executed");
            if (list != null ) {
                const nextBen3 = document.getElementById('next3')
                nextBen3.addEventListener("click", () => {
                    displayAlert("Figure recognition started");
                    StartFigureRecognition()
                    list = null;
                })
            }
        })
}

//today
function StartFigureRecognition() {
    fetch(`http://127.0.0.1:5000/StartFigureRecognition`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(resp => resp.json())
        .then(listt => {
            console.log(listt)

            fetch(`http://127.0.0.1:5000/SaveFigureData`,{
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({'age': listt[0], 'gender':listt[1]})
            }).then(resp=>resp.json())
                .then(figData => {
                    console.log(figData)
                })
            displayAlert("Figure recognition & identification is successfully executed");
        })
}

if (submitBtn != null) {
    submitBtn.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(path)

        const newData = {
            name: name.value,
            path: path.value
        }

        if (newData.path != "") {
            insertVideo(newData)
        } else {
            alert("Choose a file")
        }

    })
}

//For abnormal behaviour
function insertVideoAbnormal(newVideo) {
    fetch('http://127.0.0.1:5000/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newVideo)
    })
        .then(resp => resp.json())
        .then((data) => {

            console.log(data)
            console.log(data.id)
            //data.path = "E:\\BACKBONE\\videos\\Input.mp4"
            let id = data.id

            fetch(`http://127.0.0.1:5000/startAbnormalBehaviourDetection`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(resp => resp.json())
                .then(list => {
                    //console.log('return -> ' + list)

                })

        })
        .catch(error => console.log('error'))
}

if (submitBtnAbnormal != null) {
    submitBtnAbnormal.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(path)

        const newData = {
            name: name.value,
            path: path.value
        }

        if (newData.path != "") {
            insertVideoAbnormal(newData)
        } else {
            alert("Choose a file")
        }

    })

}

if (submitBtnFace != null) {
    submitBtnFace.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(path)

        const newData = {
            name: name.value,
            path: path.value
        }

        if (newData.path != "") {
            insertFaceVideo(newData)
        } else {
            alert("Choose a file")
        }

    })

}

//For Face Recognition
function insertFaceVideo(newVideo) {
    fetch(`http://127.0.0.1:5000/add`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newVideo)
    })
        .then(resp => resp.json())
        .then((data) => {
            // debugger

            console.log(data)
            console.log(data.id)

            let id = data.id

            fetch(`http://127.0.0.1:5000/RunFaceRecognition/${id}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data),
            })
                .then(resp => resp.json())
                .then(list => {
                    console.log(list)

                })
        }).catch(error => console.log('error'))
}

if (submitButtonFigure != null) {
    submitButtonFigure.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(path)

        const newData = {
            name: name.value,
            path: path.value
        }

        if (newData.path != "") {
            insertFigureVideo(newData)
        } else {
            alert("Choose a file")
        }

    })
}

function insertFigureVideo(newData) {
    fetch(`http://127.0.0.1:5000/RunFigureRecognition`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newData)
    })
        .then(resp => resp.json())
        .then((data) => {

            const figureData = {
                age: data[0],
                gender: data[1],
                height: 0
            }

            console.log(figureData)

            fetch(`http://127.0.0.1:5000/SaveFigureData`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(figureData)
            })
                .then(resp => resp.json())
                .then((resp) => {
                    console.log(resp);
                })
        })
        .catch(error => console.log('error'))
}

if (mainSubmitBtn != null) {
    mainSubmitBtn.addEventListener('click', (e) => {
        e.preventDefault()

        console.log(path)

        const newData = {
            name: name.value,
            path: path.value
        }

        if (newData.path != "") {
            insertVideo(newData)
        } else {
            alert("Choose a file")
        }
    })
}

function displayAlert(message){
           $('.alert').addClass("show");
           $('.alert').removeClass("hide");
           $('.alert').addClass("showAlert");
           $('.msg').text(message);
           setTimeout(function(){
             $('.alert').removeClass("show");
             $('.alert').addClass("hide");
           },5000);
         $('.close-btn').click(function(){
           $('.alert').removeClass("show");
           $('.alert').addClass("hide");
         });
}