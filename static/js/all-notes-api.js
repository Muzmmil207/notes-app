let notesContainer = document.querySelector('.all-notes')

let url = '/api/all-notes'
fetch(url)
    .then(response => response.json())
    .then(function (data) {
        console.log(data)
        let notes = data.results
        for (let i = 0; i < notes.length; i++) {

            notesContainer.innerHTML += `<a href="${notes[i]['id']}">${notes[i].title}</a>`
        }
    })

