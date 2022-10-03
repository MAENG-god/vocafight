function vocaEdit(id, vocabularyId){
    var vocaClass = ".voca_" + id;
    var voca = document.querySelector(vocaClass);
    var editForm = document.querySelector(".hidden_voca_" + id)
    voca.remove()

    var editEng = document.createElement('input');
    var editKor = document.createElement('input');
    var submitBtn = document.createElement('input');

    editEng.className = 'eng'
    editEng.setAttribute("type", "text");
    editEng.setAttribute("name", "eng");

    editKor.className = 'kor'
    editKor.setAttribute("type", "text");
    editKor.setAttribute("name", "kor");

    submitBtn.className = 'btn submitBtn';
    submitBtn.setAttribute("value", "확인");
    submitBtn.setAttribute("type", "submit");

    editForm.appendChild(editEng);
    editForm.appendChild(editKor);
    editForm.appendChild(submitBtn)

    editForm.style.visibility = "visible";
}