var map
let geolocation
let curPosition
let myPosPoint
let taskPoint
ymaps.ready(init)

function init () {
    geolocation = ymaps.geolocation

    geolocation.get().then(function (res) {
        curPosition = res.geoObjects.position
        map = new ymaps.Map('map', {
            center: curPosition,
            zoom: 18
        }, {
            searchControlProvider: 'yandex#search',
            minZoom: 14
        })

        myPosPoint = new ymaps.Placemark(curPosition, {}, {
            iconLayout: 'default#image',
            iconImageHref: 'https://cdn-icons-png.flaticon.com/512/7902/7902149.png',
            iconImageSize: [50, 50],
            iconImageOffset: [-25, -50]
        })

        taskPoint = new ymaps.Placemark([0, 0], {}, {
            iconLayout: 'default#image',
            iconImageHref: 'https://cdn-icons-png.flaticon.com/512/7151/7151488.png',
            iconImageSize: [50, 50],
            iconImageOffset: [-25, -50],
            balloonPanelMaxMapArea: 0,
            draggable: "true",
            openEmptyBalloon: true
        })

        map.controls.remove('rulerControl')
        map.controls.remove('searchControl')
        map.controls.remove('trafficControl')
        map.controls.remove('fullscreenControl')
        map.geoObjects.add(myPosPoint)
        map.geoObjects.add(taskPoint)
    })

    setInterval(function () {
        geolocation.get().then(function (res) {
            curPosition = res.geoObjects.position
            myPosPoint.geometry.setCoordinates(curPosition)
            let data = {
                'latitude': curPosition[0],
                'longitude': curPosition[1]
            }
            xhr_request('POST', '/set_position', true, data, null)
        })
    }, 1000)

    setInterval(function () {
        xhr_request('GET', '/update', true, null, function () {
            if (xhr.readyState == 4) {
                response = xhr.responseText
                if (response != 'error') {
                    json = JSON.parse(response)
                    let pointPos = [json.latitude, json.longitude]
                    taskPoint.geometry.setCoordinates(pointPos)
                    taskPoint.properties.set('balloonContent', json.point_name);
                }
            }
        })
    }, 2000)
}

function exit_session() {
    if (confirm('Вы уверены, что хотите выйти?')) {
        xhr_request('GET', '/exit_session', false, null, function() {
            if (xhr.readyState == 4) {
                if (xhr.responseText == 'ok') {
                    window.location.href = '/'
                }
            }
        })
    }
}