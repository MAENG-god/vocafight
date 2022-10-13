function vocaEdit(id){
    var vocaClass = ".voca_" + id;
    var voca = document.querySelector(vocaClass);
    var editForm = document.querySelector(".hidden_voca_" + id)
    voca.remove()
    editForm.style.display = "flex";
}