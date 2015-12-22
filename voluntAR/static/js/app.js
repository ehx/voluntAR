var app = angular.module('app', ['ngResource', 'ngRoute', 'ngCookies', 'toaster', 'ngAnimate']);

app.config(function ($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);

app.run( function($rootScope, $location) {
    $rootScope.$on( "$routeChangeStart", function(event, next, current) {
      if ( $rootScope.loggedUser === null ) {
          $location.path( "/login/" );
      }         
    });
 })


// rutas
app.config(function($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl : 'login.html',
      controller  : 'loginController'
    })

    .when('/home', {
      templateUrl : 'home.html',
      controller  : 'HomeController'
    })

    .otherwise({
      redirectTo: '/'
    });
});

// Factoriza los resource para obtener datos de la api de django
app.factory('moduleResource', function ($resource) {
  return $resource('/module/:id', {id:'@id'},
    {
      'query':  {method:'GET', isArray:true},
    });
});


app.controller('HomeController', function ($scope, $http) {

  // obtiene las tareas
  function getTasks() {
    //$scope.tasks = taskResource.query({ done: 'False'});
  }
  getTasks();

  $scope.token = $http.defaults.headers.common.Authorization

})

app.controller('loginController', function ($scope, $http, $rootScope, $location, toaster) {
  $scope.usr = {};
  $scope.submit = function() 
  {
    var data = {
            username : $scope.usr.username,
            password : $scope.usr.password
          };
    $http.post('http://localhost:8000/auth/login/', data).then(function(result){
      $http.defaults.headers.common.Authorization = 'Token ' + result.data.auth_token;
      $http.get('http://localhost:8000/auth/me/')
      .then(function(user){
        $rootScope.loggedUser = true;
        $rootScope.username = user.data.username;
        $rootScope.idUser = user.data.id;
      })
      $location.path( "/home" );
    },function() {
      $rootScope.loggedUser = null;
      $rootScope.username = '';
      $rootScope.idUser = 0;

      toaster.pop({
        type: 'error',
        title: 'Error',
        body: 'Los datos ingresados son incorrectos',
        showCloseButton: true,
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
      });
    });
  };
});


app.provider('taskProvider', function UnicornLauncherProvider() {
  var useTinfoilShielding = false;

  this.useTinfoilShielding = function(value) {
    useTinfoilShielding = !!value;
  };

  this.$get = ["apiToken", function unicornLauncherFactory(apiToken) {

    // let's assume that the UnicornLauncher constructor was also changed to
    // accept and use the useTinfoilShielding argument
    return new UnicornLauncher(apiToken, useTinfoilShielding);
  }];
});