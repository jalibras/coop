
window.onload = gradeColorCode();


function gradeColorCode(){
    var easyGrades=['3','3+','4','4+','5'];
    var mediumGrades=['5+','6A','6A+','6B','6B+'];
    var hardGrades=['6C','6C+','7A','7A+','7B','7B+','7C','7C+','8A'];
    probs = document.getElementsByClassName("problem-grade");
    for (var i=0;i<probs.length;i++) {

        if (easyGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.backgroundColor="#4c4";
        } else if (mediumGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.backgroundColor="#F0B020";
        } else if (hardGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.backgroundColor="#F03030";
        }
    }
}
