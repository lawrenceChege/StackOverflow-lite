function fetchQuestions(){
    let questions = JSON.parse(localStorage.getItem('questions'));
    let myQuestionsList = document.getElementById('myQuestionsList');
    
    myQuestionsList.innerHTML ='';
    
    for (let i=0; i<questions.length; i++){
        let Title = questions[i].Title;
        let Description = questions[i].Description;
    }

    myQuestionsList.innerHTML += '<div class="post-items">' +
                                 '<div class="question-summary">' +
                                 '<h3><a href="#">Title:' + Title+ '</a></h3>' +
                                 '<p> '+ Description +'</p'
                                 '</div></div>';
    console.log(localStorage)
}