'use strict';

var app = angular.module('app', [
  'ngResource', 
  'ngRoute', 
  'ngCookies', 
  'ngAnimate',
  'LocalStorageModule',
  'toaster'
]);

app.config(config);

function config($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;

};

app.config(['localStorageServiceProvider', function(localStorageServiceProvider){
  localStorageServiceProvider.setPrefix('ls');
}])

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);

var onlyLoggedIn = function ($location, localStorageService) {
    var user = localStorageService.get('user');
    if (user) {
      return true;
    } else {
      $location.url('/login');
    }
};

// rutas
app.config(config)

function config($routeProvider) {
  $routeProvider
    .when('/login', {
      templateUrl : 'login.html',
      controller  : 'loginController'
    })

    .when('/', {
      templateUrl : 'projects.html',
      controller  : 'projectsController',
      resolve: { loggedIn: onlyLoggedIn }
    })

    .when('/plain', {
      templateUrl : 'plain.html',
    })

    .otherwise({
      redirectTo: '/'
    });
};


// Factoriza los resource para obtener datos de la api de django
app.factory('moduleResource', moduleResource);

function moduleResource($resource) {
  return $resource('/module/:id', {id:'@id'}, {
    'query' : {method:'GET', isArray:true},
  });
};


app.controller('projectsController', homeController)

function homeController($scope, $http, $rootScope, localStorageService) {
  var user = localStorageService.get('user');
  $scope.user = user.data.username;
};


app.controller('loginController', loginController)

function loginController($scope, $http, $rootScope, $location, toaster, localStorageService) {

  $scope.usr = {};
  $scope.login = function() 
  {
    var data = {
      username : $scope.usr.username,
      password : $scope.usr.password
    };
    $http.post('http://localhost:8000/auth/login/', data).then(function(result){
      // obtengo token de auth
      $http.defaults.headers.common.Authorization = 'Token ' + result.data.auth_token;

      // obtengo datos del usuario y levanto bandera de login.
      $http.get('http://localhost:8000/auth/me/').then(function(user){
        localStorageService.set('user', user);
        //$rootScope.loggedUser = true;
        //$rootScope.username = user.data.username;
        //$rootScope.idUser = user.data.id;

        // redirigo la ruta
        $location.path( "/" );
      });
    },function() {
      $rootScope.loggedUser = null;
      $rootScope.username = '';
      $rootScope.idUser = 0;

      // muestro error por login incorrecto
      toaster.pop({
        type: 'error',
        title: 'Error',
        body: 'Los datos ingresados son incorrectos.',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
      });
    });
  };

  $scope.register = function() {
    var data_register = {
      username : $scope.usr.new_username,
      password : $scope.usr.new_password,
    };

    // Registro usuario
    $http.post('http://localhost:8000/auth/register/', data_register).then(function(result){
        // Una vez registrado , logueo usuario
        $http.post('http://localhost:8000/auth/login/', data_register).then(function(result){

        // obtengo token de auth
        $http.defaults.headers.common.Authorization = 'Token ' + result.data.auth_token;

        // obtengo datos del usuario y levanto bandera de login.
        $http.get('http://localhost:8000/auth/me/').then(function(user){
          $rootScope.loggedUser = true;
          $rootScope.username = user.data.username;
          $rootScope.idUser = user.data.id;
        });

        // redirigo la ruta
        $location.path( "/" );
      });
    });
  };
};


app.provider('taskProvider', UnicornLauncherProvider)

function UnicornLauncherProvider() {
  var useTinfoilShielding = false;

  this.useTinfoilShielding = function(value) {
    useTinfoilShielding = !!value;
  };

  this.$get = ["apiToken", function unicornLauncherFactory(apiToken) {
    return new UnicornLauncher(apiToken, useTinfoilShielding);
  }];
};