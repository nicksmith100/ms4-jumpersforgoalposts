$(document).ready(function(){

    /* Delete FAQ */

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
        e.target.parentElement.previousElementSibling.innerHTML="Delete";
        e.target.parentElement.previousElementSibling.disabled=false;
    }
    
});