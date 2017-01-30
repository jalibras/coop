
window.onload = gradeColorCode();

function gradeColorCode(){
    var easyGrades=['3','3+','4','4+','5'];
    var mediumGrades=['5+','6A','6A+','6B','6B+'];
    var hardGrades=['6C','6C+','7A','7A+','7B','7B+','7C','7C+','8A'];
    var otherGrades=['?'];
    probs = document.getElementsByClassName("problem-grade");
    for (var i=0;i<probs.length;i++) {

        if (easyGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#0a0";
        } else if (mediumGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#eeb700";
        } else if (hardGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#F01020";
        }
        else {
            probs[i].style.color="grey";
        }
    }
}


function newGradeColorCode(){
    var grades = [
        '3',
        '3+',
        '4',
        '4+',
        '5',
        '5+',
        '6A',
        '6A+',
        '6B',
        '6B+',
        '6C',
        '6C+',
        '7A',
        '7A+',
        '7B',
        '7B+',
        '7C',
        '7C+',
        '8A',
        '8A+',
        '8B',
        '8B+',
        '8C',
        '8C+',
        ];

    var easyGrades=['3','3+','4','4+','5'];
    var mediumGrades=['5+','6A','6A+','6B','6B+'];
    var hardGrades=['6C','6C+','7A','7A+','7B','7B+','7C','7C+','8A'];
    var otherGrades=['?'];
    probs = document.getElementsByClassName("problem-grade");
    for (var i=0;i<probs.length;i++) {

        if (easyGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#0a0";
        } else if (mediumGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#eeb700";
        } else if (hardGrades.indexOf(probs[i].getAttribute("data"))>=0){
            probs[i].style.color="#F01020";
        }
        else {
            probs[i].style.color="grey";
        }
    }
}

function rowClickHandler(el){
    window.document.location = el.getAttribute("data-href");
}
