    // Функция ymaps.ready() будет вызвана, когда
    // загрузятся все компоненты API, а также когда будет готово DOM-дерево.

    ymaps.ready(init);

    function init() {
        var coordinates = [[55.75148, 37.610242], [55.752353, 37.610855], [55.752605, 37.611161], [55.754339, 37.612086], [55.754554, 37.612248], [55.756214, 37.607055], [55.757763, 37.608925], [55.758315, 37.609781], [55.759164, 37.611731], [55.758138, 37.612906], [55.756959, 37.61496], [55.756556, 37.61483], [55.75569, 37.613876], [55.755767, 37.614535]]

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
