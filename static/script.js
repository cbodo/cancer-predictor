'use strict';

function get_modal(img) {
    var modal = document.getElementById("modal");
    var imgUrl = document.getElementById(img.src);
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