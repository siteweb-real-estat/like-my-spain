document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('map').setView([0, 0], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var properties = JSON.parse(document.getElementById('property-data').textContent);

    properties.forEach(function(property) {
        var fields = property.fields;
        var marker = L.marker([fields.latitude, fields.longitude]).addTo(map);
        marker.bindPopup('<b>' + fields.title + '</b><br>' + fields.description + '<br>Price: $' + fields.price);
    });
});