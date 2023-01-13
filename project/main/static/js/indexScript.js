function create_group(el) {
    let popup_window = el.closest(".popup_container")
    let error_div = popup_window.querySelector('.error')

    let group_name = popup_window.querySelector("input[name='group_name']")
    let card_id = popup_window.querySelector("input[name='card_id']")

    if (group_name.value == "" || card_id.value == "") {
        error_div.classList.remove('disable')
        error_div.innerHTML = "Одно из полей не заполнено"
        return
    }

    let data = {group_name: group_name.value, card_id: card_id.value}
    xhr_request('POST', '/create_new_group', true, data, function () {
        if (xhr.readyState == 4) {
            if (xhr.responseText == 'ok') {
                window.location.href = '/'
            } else {
                error_div.innerHTML = xhr.responseText
                error_div.classList.remove('disable')

            }
        }
    })
}

function join_group(el) {
    let popup_window = el.closest(".popup_container")
    let error_div = popup_window.querySelector('.error')
    let group_name = popup_window.querySelector("input[name='group_name']")

    if (group_name.value == "") {
        error_div.classList.remove('disable')
        error_div.innerHTML = "Одно из полей не заполнено"
        return
    }

    let data = {group_name: group_name.value}
    xhr_request('POST', '/join_group', true, data, function () {
        if (xhr.readyState == 4) {
            if (xhr.responseText == 'ok') {
                window.location.href = '/'
            } else {
                error_div.innerHTML = xhr.responseText
                error_div.classList.remove('disable')
            }
        }
    })
}