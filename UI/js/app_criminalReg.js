const myform  = document.getElementById('myform')
const Name = document.getElementById('Name')
const Age = document.getElementById('Age')
const Gender = document.getElementById('Gender')
const DOB = document.getElementById('DOB')
const Address = document.getElementById('Address')
const Blood_Group = document.getElementById('Blood_Group')
const NIC = document.getElementById('NIC')
const Height = document.getElementById('Height')
const Crimes = document.getElementById('Crimes')
const fileinput = document.getElementById('fileinput')

//Get Criminal Details
const criminals = document.getElementById('criminals')


const insertData = (newCriminal) => {
    fetch('http://localhost:5000/add_Criminals',{
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify(newCriminal)
    })
        .then(resp => resp.json())
        .then((data) => {
            console.log(data)
        })
        .catch(error => console.log(error))
}

myform.addEventListener('submit', (e) => {
    e.preventDefault()

    const newCriminal = {
        Name:Name.value,
        Age:Age.value,
        Gender:Gender.value,
        DOB:DOB.value,
        Address:Address.value,
        Blood_Group:Blood_Group.value,
        NIC:NIC.value,
        Height:Height.value,
        Crimes:Crimes.value,
        fileinput:fileinput.value
    }

    insertData(newCriminal)
    console.log("error")
})

const getAllData = () => {
    fetch("http://localhost:5000/get_Criminals", {
        method:'GET',
        headers:{
            'Content-Type':'application/json'
        }
    })
        .then(resp => resp.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
}
