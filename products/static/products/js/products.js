$(document).ready(function(){

    /*---Page features---*/

    /* Flip-card */
    $("#product-container").on("click", ".flip-card", function(e) {
        if($(e.target).is("a")) {
            return true;
        } else if($(e.target).is("button")) {
            return true;
        } else if($(e.target).is("img")) { 
            return false;
        } else { this.classList.toggle("flipped"); }
    });

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


    /*---Add and remove products---*/

    /* Get CSRF token to allow add-to-bag function to work */
    /* Code from: https://docs.djangoproject.com/en/5.0/howto/csrf/ */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    /* Add-to-bag (Code adapted from https://www.youtube.com/watch?v=PgCMKeT2JyY) */
    let addBtns = document.querySelectorAll(".add-btn")
    addBtns.forEach(addBtn=>{
        addBtn.addEventListener("click", addToBag)
    })
    function addToBag(e){
        let productId = e.target.value;
        let url = addUrl;

        let data = {
            id: productId,
        };
        fetch(url, {
            method: "POST",
            headers: {"Accept":"application/json", "X-Requested-With": "XMLHttpRequest", "X-CSRFToken": csrftoken},
            body: JSON.stringify(data)
        })
        .then(response => {
            return response.json();
        })
       
        /* This block is custom code not from above source */
        .then(e.target.classList.remove("d-block"))
        .then(e.target.classList.add("d-none"))
        .then(e.target.nextElementSibling.classList.remove("d-none"))
        .then(e.target.nextElementSibling.classList.add("d-block"))
        
        .then(data=>{
            document.getElementById("product-count").innerHTML = ` ${data.product_count} `;
            document.getElementById("bag-total").innerHTML = `<span class="fw-bold">£${data.bag_total}</span>`;
        })
        .then(() => {
            $( "#message-container" ).load(window.location.href + " #message-container" )
        })
        .catch(error=>{
            console.log(error);
        });
    }

    /* Remove-from-bag (products page) */
    /* (Code adapted from https://www.youtube.com/watch?v=PgCMKeT2JyY) */
    let removeBtns = document.querySelectorAll(".remove-btn")
    removeBtns.forEach(removeBtn=>{
        removeBtn.addEventListener("click", removeFromBag)
    })
    function removeFromBag(e){
        let productId = e.target.value;
        let url = removeUrl;
        let data = {
            id: productId,
        };
        fetch(url, {
            method: "POST",
            headers: {"Accept":"application/json", "X-Requested-With": "XMLHttpRequest", "X-CSRFToken": csrftoken},
            body: JSON.stringify(data)
        })
        .then(response => {
            return response.json();
        })

        /* This block is custom code not from above source */
        .then(e.target.classList.remove("d-block"))
        .then(e.target.classList.add("d-none"))
        .then(e.target.previousElementSibling.classList.remove("d-none"))
        .then(e.target.previousElementSibling.classList.add("d-block"))
        
        .then(data=>{
            document.getElementById("product-count").innerHTML = ` ${data.product_count} `;
            document.getElementById("bag-total").innerHTML = `<span class="fw-bold">£${data.bag_total}</span>`;
        })
        .then(() => {
            $( "#message-container" ).load(window.location.href + " #message-container" )
        })
        .catch(error=>{
            console.log(error);
        });
    }

    /* Delete product (products page admin) */
    
    /* Display confirmation and cancel links */
    let deleteBtns = document.querySelectorAll(".delete-btn")
    deleteBtns.forEach(deleteBtn=>{
        deleteBtn.addEventListener("click", showDeleteConfirmationBtn)
    })
    function showDeleteConfirmationBtn(e){
        e.target.innerHTML="Are you sure?";
        e.target.disabled=true;
        e.target.nextElementSibling.classList.remove("d-none");
        e.target.nextElementSibling.classList.add("d-block");
    }

    /* Hide confirmation and cancel links */
    let deleteCancelLinks = document.querySelectorAll(".delete-cancel")
    deleteCancelLinks.forEach(deleteCancelLink=>{
        deleteCancelLink.addEventListener("click", hideDeleteConfirmationBtn)
    })
    function hideDeleteConfirmationBtn(e){
        e.target.parentElement.classList.remove("d-block");
        e.target.parentElement.classList.add("d-none");
        e.target.parentElement.previousElementSibling.innerHTML="Delete product";
        e.target.parentElement.previousElementSibling.disabled=false;
    }

});