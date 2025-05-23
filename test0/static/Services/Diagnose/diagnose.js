const form = document.querySelector("form"),
    fileInput = form.querySelector(".file-input"),
    progressArea = document.querySelector(".progress-area"),
    uploadedArea = document.querySelector(".uploaded-area");
var check=true; 
function submit(){
    var count1=fileInput.files.length;
    if( count1>0){
        form.submit();
    }
    else{
        alert("please choose file");
    }
 };

form.addEventListener("click", () => {
    if(check){
      fileInput.click();
    }
    
}); 
fileInput.onchange =({ target }) => {
    let file = target.files[0]; //getting file and [0] means if user has selected multi files >get first file only
    if (file) { // if file is selected
        let fileName = file.fileName; //getting selected file name
       // uploadFile(fileName); //calling uploadfile with passing file name as an argument
    }
};

// //////////////////////////////////////////////////////////////////////////////

// const ctx = document.getElementById('doughnut').getContext('2d');
// const doughnut = new Chart(ctx, {
//     type: 'doughnut',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });