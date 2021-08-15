
let questions = [];

questn = {
    quest:'Where is the capital of Nigeria',
    opt_a: 'Lagos',
    opt_b: 'Kaduna',
    opt_c: 'Abuja',
}

correctAns = questn.opt_c;


questions.push(questn)

function ansResponse(response) {
    correct = response;
}

const wrong = ansResponse("Your answer is wrong")

question.innerHTML =questn.quest;
optionA.innerText = questn.opt_a;
optionB.innerText = questn.opt_b;
optionC.innerText = questn.opt_c;

function result(answer) {
    if (correctAns = answer) {
        ans.innerText = 'your answer was correct'
    }else {
        ans.innerText = 'Your answer was Wrong'
    }
}
responseA.onclick = () => result();
responseB.onclick = () => result();
responseC.onclick = () => result(correctAns);

// responseA.addEventListener('click', result())


// const api_url = "http://127.0.0.1:5000/"

// async function getQuestions(url) {
//     const response = await fetch(url)
//     var data = await response.json()
//     console.log(data)

//     showData(data)
// }

// function showData(data) {
//     for (let q in data.list) {
//         question.innerHTML =q.quest;
//         optionA.innerText = q.optionA;
//         optionB.innerText = q.optionB;
//         optionC.innerText = q.optionC;
//     }
// }
