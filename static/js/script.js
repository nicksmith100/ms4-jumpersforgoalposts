$(document).ready(function(){

    /* Event listener for flip-card function */

    $(".product-container").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else { this.classList.toggle("flipped"); }
    });

});