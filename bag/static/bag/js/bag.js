$(document).ready(function(){

    /* Get CSRF token to allow remove-from-bag function to work */
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

    /* Remove-from-bag (bag page) */

    /* Display confirmation and cancel buttons */
    let bagRemoveBtns = document.querySelectorAll(".bag-remove-btn")

    bagRemoveBtns.forEach(bagRemoveBtn=>{
        bagRemoveBtn.addEventListener("click", showConfirmationBtn)
    })
    function showConfirmationBtn(e){
        
        e.target.innerHTML="Are you sure?";
        e.target.disabled=true;
        e.target.nextElementSibling.classList.remove("d-none");
        e.target.nextElementSibling.classList.add("d-block");
       
    }

    /* Remove from bag if confirmed */
    let confirmBtns = document.querySelectorAll(".confirm-btn")
    confirmBtns.forEach(confirmBtn=>{
        confirmBtn.addEventListener("click", removeFromBagView)
    })
    function removeFromBagView(e){
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
        .then(data=>{
            document.getElementById("product-count").innerHTML = ` ${data.product_count} `;
            document.getElementById("bag-total").innerHTML = `<span class="fw-bold">£${data.bag_total}</span>`;
        })
        .catch(error=>{
            console.log(error);
        })
        .then(() => {
            location.reload()
        })
    }

    /* Cancel removal */
    let cancelBtns = document.querySelectorAll(".cancel-btn")
    cancelBtns.forEach(cancelBtn=>{
        cancelBtn.addEventListener("click", hideConfirmationBtn)
    })
    function hideConfirmationBtn(e){
        
        e.target.parentElement.classList.remove("d-block");
        e.target.parentElement.classList.add("d-none");
        e.target.parentElement.previousElementSibling.innerHTML="Remove item";
        e.target.parentElement.previousElementSibling.disabled=false;
    }
    
});