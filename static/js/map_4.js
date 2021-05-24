    // Функция ymaps.ready() будет вызвана, когда
    // загрузятся все компоненты API, а также когда будет готово DOM-дерево.

    ymaps.ready(init);

    function init() {
        var coordinates = [[59.937129, 30.31247], [59.931096, 30.360964], [59.934163, 30.362846], [59.934285, 30.36021], [59.934736, 30.360217]]

        // Создание карты.
        // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/map-docpage/
        var myMap = new ymaps.Map("map", {
            // Координаты центра карты.
            // Порядок по умолчнию: «широта, долгота».
            center: [49.084340, 8.944410],
            // Уровень масштабирования. Допустимые значения:
            // от 0 (весь мир) до 19.
            zoom: 7,
            // Элементы управления
            // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/controls/standard-docpage/
            controls: [

                'zoomControl', // Ползунок масштаба
                'rulerControl', // Линейка
                'routeButtonControl', // Панель маршрутизации
                'trafficControl', // Пробки
                'typeSelector', // Переключатель слоев карты
                'fullscreenControl', // Полноэкранный режим

                // Поисковая строка
                new ymaps.control.SearchControl({
                    options: {
                        // вид - поисковая строка
                        size: 'large',
                        // Включим возможность искать не только топонимы, но и организации.
                        provider: 'yandex#search'
                    }
                })

            ]
        });
        for (var i of coordinates) {
            myMap.geoObjects.add(new ymaps.Placemark(i));
        }
        var routeLine = new ymaps.Polyline(coordinates, {}, {strokeWidth: 4, strokeColor: '#8b00ff'});
        myMap.geoObjects.add(routeLine);
        myMap.setBounds(myMap.geoObjects.getBounds());
        // Добавление метки
        // https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/Placemark-docpage/
        //var myPlacemark = new ymaps.Placemark([55.76, 37.64], {
            // Хинт показывается при наведении мышкой на иконку метки.
        //    hintContent: 'кликните по метке чтобы узнать подробную информацию',
            // Балун откроется при клике по метке.
        //    balloonContent: 'Содержимое метки'
        //});

        // После того как метка была создана, добавляем её на карту.
        //myMap.geoObjects.add(myPlacemark);
    }
