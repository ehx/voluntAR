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

function config($httpProvider, $resourceProvider, localStorageServiceProvider, $routeProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
  localStorageServiceProvider.setPrefix('ls');

  // rutas
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


// Factoriza los resource para obtener datos de la api de django
app.factory('moduleResource', moduleResource);

function moduleResource($resource) {
  return $resource('/module/:id', {id:'@id'}, {
    'query' : {method:'GET', isArray:true},
  });
};


app.controller('projectsController', homeController)

function homeController($http, localStorageService) {
  var vm = this;
  var user = localStorageService.get('user');

  vm.user = user.data.username;
};


app.controller('loginController', loginController)

function loginController($scope, $http, localStorageService, loginService) {
  var vm = this;
  vm.usr = {};

  $scope.login = function() 
  {
    var vm = this;
    var data = {
      username : vm.usr.username,
      password : vm.usr.password
    };

    localStorageService.set('data_login', data);
    loginService.login();
  };

  $scope.register = function() {
    var vm = this;
    var data = {
      username : vm.usr.new_username,
      password : vm.usr.new_password,
    };

    // Registro usuario
    $http.post('http://localhost:8000/auth/register/', data_register).then(function(result){
      // Una vez registrado , logueo usuario
      localStorageService.set('data_login', data)
      loginService.login();
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