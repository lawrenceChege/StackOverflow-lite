function fetchQuestions() {
    let questions = JSON.parse(localStorage.getItem('questions'));
    let myQuestionsList = document.getElementById('myQuestionsList');

    myQuestionsList.innerHTML = '';

    for (let i = 0; i < questions.length; i++) {
        let Title = questions[i].Title;
        let Description = questions[i].Description;
    }

    myQuestionsList.innerHTML += '<div class="post-items">' +
        '<div class="question-summary">' +
        '<h3><a href="#">Title:' + Title + '</a></h3>' +
        '<p> ' + Description + '</p'
    '</div></div>';
    console.log(localStorage)
}

function getQuestions() {
    fetch('localhost:5000/api/v1/questions/')
        .then((res) => res.json())
        .then((data) => {
            let output = '<h2> Posts</h2>';
            data.forEach(function (post) {
                output +=`
                    <div class="post-items">
                        <div class="question-summary">
                            <h3>
                                <a href="#">${questios.title}</a>
                            </h3>
                            <p class="ans-by">answed by:${questions.user} </p>
                            <p class="last-view">last viewed on: by
                                <a href="#user">user</a>
                            </p>
                            <p class="qn-time">posted at ${questions.date_created} on 12/3/18</p>
                        </div>
                        <div class="votes">
                            <div class="mini-counts">
                                <span title=" ${questions.upvotes} votes">${questions.upvotes}</span>
                            </div>
                            <div>upvotes</div>
                        </div>
                        <div class="votes">
                            <div class="mini-counts">
                                <span title=" ${questions.downvotes} votes">${questions.downvotes}</span>
                            </div>
                            <div>downvotes</div>
                        </div>
                        <div class="accepted-answers">
                            <div class="mini-counts">
                                <span title="${questions.answers} answers">${questions.answers}</span>
                            </div>
                            <div>answers</div>
                        </div>
                        <div class="views">
                            <div class="mini-counts">
                                <span title=" 123 views"> 123</span>
                            </div>
                            <div>views</div>
                        </div>
                        <a href="anwer.html"><i class="fas fa-reply"></i></a>
                    </div>
                `;
            });
            document.getElementById('outputAPI').innerHTML = output
        })
}