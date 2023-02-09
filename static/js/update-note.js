let url = `/api/single-notes/${id}`
let form = document.getElementById('note-form')
let label = document.getElementById('id_label')
let title = document.getElementById('id_title')
let content = document.getElementById('id_content')
let remind = document.getElementById('id_remind')

remind.setAttribute('type', 'datetime-local') // Update the remind input from text to datetime-local

//  Sending Post request to the API to store the new Note
form.onsubmit = function (e) {
    e.preventDefault()
    console.log(remind.value.length)
    fetch(url, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'label': label.value,
            'title': title.value,
            'content': content.value,
            'remind': remind.value.length > 0 ? remind.value : null
        })
    })
        .then(response => response.json())
        .then((data) => {
            if (data.id) {
                location.reload()
            } else {
                alert('Error')
            }
        })
}
