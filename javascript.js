function initMap() {
        var uluru = {lat: 49.838, lng: 24.023};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 9,
          center: uluru
        });
        var marker = new google.maps.Marker({position: uluru,map: map});
        var marker2 = new google.maps.Marker({position:{lat: 49.830, lng: 24.023},map:map})
      }