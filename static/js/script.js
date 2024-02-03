$(document).ready(function(){

    /* Event listener for flip-card function */

    $(".product-container").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else { this.classList.toggle("flipped"); }
    });


    var imageModal = document.getElementById('image-modal')
    imageModal.addEventListener('show.bs.modal', function (event) {
    // Anchor that triggered the modal
    var anchor = event.relatedTarget
    // Extract info from data-bs-* attributes
    var image = anchor.getAttribute('data-bs-image')
    var imageTitle = anchor.getAttribute('data-bs-image-title')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    var modalTitle = imageModal.querySelector('.modal-title')
    var modalBody = imageModal.querySelector('.modal-body')

    modalTitle.textContent = imageTitle
    modalBody.innerHTML = `<img src="${image}" alt="${imageTitle}" class="w-100">`
    })


});