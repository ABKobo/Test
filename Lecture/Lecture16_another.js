function course_door(color_name){
    let element = document.getElementById("Python");
    element.style.color = color_name;
}

// int
let n; // n 정의 이제 사용 가능
n = 20;
const m = 10; // m 고정, 변경 불가
console.log(n+m); // 30

//str
let name = 'Ko';
let upper = name.toUpperCase();
let first = name.slice(0,1);
console.log(upper, first); // KO, K

// bool
let is = true;
let result = 10>20;
console.log(is, result); // true, false

// Array (List)
let lst = ["Ko", 20];
lst.push("Yoon"); // 추가 (append)
lst.push("Seok");
lst.pop(); // 마지막 제거
console.log(lst);

// Function
function minus(a, b){
    return a - b;
}
alert(minus(n,m)); // 창으로 표시
console.log(minus(n,m));

function course_color(color_name){
    let element = document.getElementById("Python"); // ID 로 가져오기
    element.style.color = color_name;
}

function color(color_name){
    let element = document.getElementsByClassName("student")[0]; // Class 로 가져오기 [0]: 첫 번째 student 만
    element.style.color = color_name
}

function but(color_name){
    let element = document.getElementsByTagName("button")[3]; // <h1> 같이 Tag 이름
    element.style.color = color_name
}

function que(color_name){
    let element = document.querySelector(".student"); // 전체 하나만 예: (.student) (#Python), 
    element.style.color = color_name
}

function queAll(color_name){
    let elements = document.querySelectorAll('.student'); // 전체 예: (.student) (#Python)
    elements[1].style.color = color_name //[] 필요
}