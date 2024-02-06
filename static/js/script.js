$(document).ready(function(){

    /* Flip-card */

    $("#product-container").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else if($(e.target).is("img")) { 
            return false;
        } else { this.classList.toggle("flipped"); }
    });

    /* Modal (Code from: https://getbootstrap.com/docs/5.3/components/modal/#varying-modal-content) */
    
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

    /* Sort selector (Code from: https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/656166307e469630d09e0eb17a0d17daa440e208/products/templates/products/products.html) */

    $('#sort-selector').change(function() {
        let selector = $(this);
        let currentUrl = new URL(window.location);

        let selectedVal = selector.val();
        if(selectedVal != "reset"){
            let sort = selectedVal.split("_")[0];
            let direction = selectedVal.split("_")[1];

            currentUrl.searchParams.delete("page");
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("page");
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
            
            window.location.replace(currentUrl);
        }
    })

    /* Back-to-top button */

    $('.btt-link').click(function(e) {
        window.scrollTo(0,0)
    })

});