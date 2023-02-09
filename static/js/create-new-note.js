let url = '/api/all-notes'
let form = document.getElementById('new-note')
let label = document.getElementById('id_label')
let title = document.getElementById('id_title')
// let content = document.getElementById('id_content')
let cke_editable = document.querySelector('.cke_editable')
let remind = document.getElementById('id_remind')
remind.setAttribute('type', 'datetime-local')
form.onsubmit = function (e) {
    e.preventDefault()
    console.log(remind.value)
    console.log(cke_editable)
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
            'remind': remind.value
        })
    })
        .then(response => response.json())
        .then((data) => {
            // location.href = `/note-${data.id}/`
        })

}
