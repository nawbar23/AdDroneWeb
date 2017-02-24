//Angular Map Module and Controller
var mapModule = angular.module("MapMod", []);
mapModule.controller('mapController', function ($scope) {

    var latitude = 50.033235;
    var longitude = 19.938747;
    var mapCanvas = document.getElementById("map");
    var mapOptions = {
      zoom: 15,
      center: new google.maps.LatLng(latitude,longitude),
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      draggable: false
    }

    $scope.map = new google.maps.Map(mapCanvas, mapOptions);
    $scope.lat = latitude;
    $scope.lon = longitude;

    var createMarker = function(){
      var marker = new google.maps.Marker({
        map: $scope.map,
        position: new google.maps.LatLng(latitude, longitude),
      });
    }
    createMarker();
});
