let notesContainer = document.querySelector('.all-notes')

let url = '/api/all-notes'
fetch(url)
    .then(response => response.json())
    .then(function (data) {
        console.log(data)
        notesContainer.innerHTML += `<a href="">dfsgsg</a>`
    })
console.log('fdesfrg;m')