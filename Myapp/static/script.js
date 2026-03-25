const text = ["Frontend Developer", "Web Designer", "Freelancer"];
let i = 0, j = 0;
let currentText = "";
let isDeleting = false;

function type() {
    if (i < text.length) {
        if (!isDeleting) {
            currentText = text[i].substring(0, j++);
        } else {
            currentText = text[i].substring(0, j--);
        }

        document.getElementById("typing").innerHTML = currentText;

        if (j == text[i].length) isDeleting = true;
        if (j == 0 && isDeleting) {
            isDeleting = false;
            i++;
        }
    } else {
        i = 0;
    }
    setTimeout(type, 100);
}

type();