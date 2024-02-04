$(document).ready(function(){

    /* Flip-card functionality */

    $(".product-container").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else if($(e.target).is("img")) { 
            return false;
        } else { this.classList.toggle("flipped"); }
    });

    /* Modal functionality */
    
    let imageModal = document.getElementById('image-modal')
    imageModal.addEventListener('show.bs.modal', function (event) {
    
        // Anchor that triggered the modal
        let anchor = event.relatedTarget
        
        // Extract info from data-bs-* attributes
        let image = anchor.getAttribute('data-bs-image')
        let imageTitle = anchor.getAttribute('data-bs-image-title')

        // Update the modal's content.
        let modalTitle = imageModal.querySelector('.modal-title')
        let modalBody = imageModal.querySelector('.modal-body')

        modalTitle.textContent = imageTitle
        modalBody.innerHTML = `<img src="${image}" alt="${imageTitle}" class="w-100">`
    
    })


});