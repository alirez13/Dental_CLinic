function like(pk) {
    var element = document.getElementById('like')
    var element2 = document.getElementById('like-out')
    var count = document.getElementById('count')
    $.get(`/like/${pk}/`).then(response => {
        if (response['result'] === 'liked') {
            element.className = "love active"
            element2.className = "fa fa-heart"
            count.innerText = Number(count.innerText) + 1
        } else {
            element.className = "love"
            element2.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText) - 1
        }
    })
}