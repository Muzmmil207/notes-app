let category = document.getElementById('category')
let date = document.getElementById('date')
let title = document.getElementById('title')
let content = document.getElementById('content')
let notesContainer = document.getElementById('notes')
let url = '/api/all-notes'
async function GetNotes() {
    let response = await fetch(url)
    let data = await response.json()
    console.log(data)
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
                    ${notes[i].content || ''}
                </a>
            </div>
        </div>
            `
    }
}
GetNotes()