function route($provider){
    $provider.when('/:tag',{
        templateUrl: 'partials/tag.html',
        controller:'TagCtrl'
    }).otherwise({
        redirectTo:'/'
    });
}
