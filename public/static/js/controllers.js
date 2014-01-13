var engfordevControllers= angular.module('engfordevControllers',[]);

engfordevControllers.controller('IndexCtrl', ['$scope', '$http', indexController]);

function indexController($scope, $http){
    console.log("test");
}
