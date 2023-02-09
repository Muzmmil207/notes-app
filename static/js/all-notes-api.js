let url = '/api/all-notes'

let category = document.getElementById('category')
let date = document.getElementById('date')
let title = document.getElementById('title')
let content = document.getElementById('content')
let notesContainer = document.getElementById('notes')

async function GetNotes(query = null) {
    if (query !== null) {
        url = url + `?search=${query.replace(' ', '+')}`
    }

    let response = await fetch(url)
    let data = await response.json()
    let notes = data.results

    for (let i = 0; i < notes.length; i++) {

        notesContainer.innerHTML += `
            <div class="note">
            <div class="head">
                <div class="category" id="category">${notes[i].category || ''} </div>
                <div class="date" id="date">${notes[i].updated_at}</div>
            </div>
            <div class="content">
                <a href="note-${notes[i]['id']}" class="title" id="title">${notes[i].title || ''}</a>
                <a href="note-${notes[i]['id']}" class="note-text" id="content">
                    ${notes[i]['content'].slice(0, 100) || ''}...
                </a>
            </div>
        </div>
            `
    }
    url = '/api/all-notes'
}
GetNotes()

let searchForm = document.getElementById('search-form')
let = searchInput = document.getElementById('search-input')

searchForm.addEventListener('submit', function (e) {
    e.preventDefault()
    notesContainer.innerHTML = ''
    GetNotes(searchInput.value)
})