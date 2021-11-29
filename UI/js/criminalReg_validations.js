const previewContainer = document.getElementById("preview");
const previewImages = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text")

fileinput.addEventListener("change", function () {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        previewDefaultText.style.display = "none";
        previewImages.style.display = "block";

        reader.addEventListener("load", function () {
            previewImages.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    } else {
        previewDefaultText.style.display = null;
        previewImages.style.display = null;
        previewImages.setAttribute("src", "")
    }
});

// Character Check
function lettersValidate(key) {
    var keycode = (key.which) ? key.which : key.keyCode;

    if ((keycode > 64 && keycode < 91) || (keycode > 96 && keycode < 123)) {
        return true;
    } else {
        return false;
    }
}

// Number Check
function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}


$('#submit-button').on("click", function () {
    let valid = true;
    $('[required]').each(function () {
        if ($(this).is(':invalid') || !$(this).val()) valid = false;
    })
    if (!valid) {
        Swal.fire({
            icon: 'warning',
            title: 'Unsuccessful',
            text: 'Fill All Details!'
        });
    } else {
        Swal.fire({
            icon: 'success',
            title: 'Successfully Registered!',
            text: 'Please wait Criminals images are Training!',
            html: 'Training will Complete with in <b><b> Minutes.',
            timer: 30000,
            showConfirmButton: false,
            timerProgressBar: true,
            allowOutsideClick: false,
            allowEscapeKey: false,
            closeOnClickOutside: false,
            didOpen: () => {
                Swal.showLoading()
                const b = Swal.getHtmlContainer().querySelector('b')
                timerInterval = setInterval(() => {
                    b.textContent = Swal.getTimerLeft()
                }, 1000)
            },
            willClose: () => {
                clearInterval(timerInterval)
            }
        }).then((result) => {
            /* Read more about handling dismissals below */
            if (result.dismiss === Swal.DismissReason.timer) {
                console.log('I was closed by the timer')
            }
        }, setTimeout(function () {
            window.location.href = 'home.html';
        }, 30000));
    }
})

// function previewImages() {
//
//     var preview = document.querySelector('#preview');
//
//     if (this.files) {
//         [].forEach.call(this.files, readAndPreview);
//     }
//
//     function readAndPreview(file) {
//
//         // Make sure `file.name` matches our extensions criteria
//         if (!/\.(jpe?g|png|gif)$/i.test(file.name)) {
//             return alert(file.name + " is not an image");
//         } // else...
//
//         var reader = new FileReader();
//
//         reader.addEventListener("load", function () {
//             var image = new Image();
//             image.height = 500;
//             image.width = 500;
//             image.title = file.name;
//             image.src = this.result;
//             preview.appendChild(image);
//         });
//
//         reader.readAsDataURL(file);
//     }else{
//         previewDefaultText.style.display = null;
//         previewImages.style.display = null;
//         previewImages.setAttribute("src","")
//     }
// }document.querySelector('#fileinput').addEventListener("change", previewImages);
