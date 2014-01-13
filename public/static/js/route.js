function route($provider){
    $provider.when('/',{
        controller:'IndexCtrl'
    })
    .when('/:tag',{
        templateUrl: 'partials/tag.html',
        controller:'TagCtrl'
    }).otherwise({
        redirectTo:'/'
    });
}
