'use strict';

window.onload = function() {
    var currentDate = new Date();
    document.getElementById('current-year').innterHTML = currentDate.getFullYear();
}

function closeContents() {
    let offcanvas = document.getElementById("offcanvasRight");
    let openCanvas = bootstrap.Offcanvas.getInstance(offcanvas);
    openCanvas.hide();
}

function getModal(img) {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById('modal-img');
    var captionText = document.getElementById("caption");

    modal.style.display = "block";
    var url = img.src.split("/")
    modalImg.src = '../static/images/' + url[url.length - 1];
    captionText.innerHTML = img.alt;

    // Closes modal via 'X' button
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
    }
}