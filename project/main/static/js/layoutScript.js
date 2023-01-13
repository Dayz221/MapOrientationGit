function exit_popup(el) {
    let popup_window = el.closest(".popup_container")
    popup_window.classList.add("disable")
}

function open_popup(id_) {
    let popup = document.querySelector(id_)
    popup.classList.remove("disable")
}

function popup_input(el) {
    let popup = el.closest(".popup_container")
    let error_div = popup.querySelector('.error')
    error_div.classList.add("disable")
}

function xhr_request(method, target, async, data, function_) {
    xhr = new XMLHttpRequest()
    xhr.open(method, target, async)
    xhr.onreadystatechange = function_
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')

    let data_ = ""
    count = 0
    for (let key in data) {
        if (count != 0) data_ += '&'
        data_ += key + '=' + data[key]
        count++
    }

    xhr.send(data_)
}
