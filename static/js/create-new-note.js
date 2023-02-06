let url = '/api/all-notes'
let form = document.getElementById('new-note')
let label = document.getElementById('id_label')
let title = document.getElementById('id_title')
let content = document.getElementById('id_content')
let remind = document.getElementById('id_remind')
let csrfToken = document.getElementsByName('csrfmiddlewaretoken')

form.onsubmit = function (e) {
    e.preventDefault()

    console.log(csrftoken)
    console.log(title.value)
    console.log(label.value)
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
        })
    })
        .then(() => {
            console.log('----')
        })

}
