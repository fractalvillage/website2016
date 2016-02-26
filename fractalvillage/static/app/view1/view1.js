'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: '/static/app/view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', 'getVillages', function($scope,getVillages) {
  getVillages(function(villages) {
    $scope.villages = villages;
  });
}])

.service('getVillages', ['$http', function($http) {
  return function(callback) {
    return $http.get('v1/villages').then(function(response) {
      callback(response.data.results);
    });
  };
}]);
