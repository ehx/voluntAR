'use strict';

var app = angular.module('app', [
  'ngResource',
  'ngRoute',
  'ngCookies',
  'ngAnimate',
  'LocalStorageModule',
  'toaster',
]);

app.config(config);

function config($httpProvider, $resourceProvider, localStorageServiceProvider, $routeProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  //$resourceProvider.defaults.stripTrailingSlashes = false;
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

    .when('/evento/:id', {
      templateUrl : 'event.html',
      controller  : 'eventController',
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

app.directive('tabsJquery', tabsJquery);

function tabsJquery() {
  return {
    restrict: 'A',
    link: function(scope, elm, attrs) {
      var jqueryElm = $(elm[0]);
      $(jqueryElm).tabs()
    }
  };
}

var onlyLoggedIn = function ($location, localStorageService) {
  var user = localStorageService.get('user');
  if(user) {
    return true;
  } else {
    $location.url('/login');
  }
};


// Factoriza los resource para obtener datos de la api de django
app.factory('eventResource', function ($resource) {
  return $resource('/evento/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PATCH'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'}
    });
});

app.factory('accountResource', function ($resource) {
  return $resource('/cuenta/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PATCH'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'}
    });
});

app.factory('eventBackResource', function ($resource) {
  return $resource('/evento_aporte/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PATCH'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'}
    });
});

app.factory('eventVoluntaryResource', function ($resource) {
  return $resource('/evento_voluntario/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PATCH'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'}
    });
});

app.factory('moduleResource', moduleResource);

function moduleResource($resource) {
  return $resource('/module/:id', {id:'@id'}, {
    'query' : {method:'GET', isArray:true},
  });
};

// Factoriza los resource para obtener datos de la api de django
app.factory('eventResource', function ($resource) {
  return $resource('/evento/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PATCH'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'}
    });
});

app.controller('projectsController', projectsController)

function projectsController($scope, $http, localStorageService, eventResource) {
  var vm = this;
  var user = localStorageService.get('user');

  vm.user = user.data.username;


  eventResource.query({}, function(data){
		$scope.eventos = data;
	});
};


app.controller('loginController', loginController)

function loginController($scope, $http, localStorageService, loginService, toaster) {
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
    $http.post('http://localhost:8000/auth/register/', data).then(function(result){
      // Una vez registrado , logueo usuario
      localStorageService.set('data_login', data)
      loginService.login();
    }, function(response){
      // Mestra mensaje en caso de no poder registrar usuario.
      toaster.pop({
        type: 'error',
        title: 'Error',
        body: 'El usuario ya esta registrado.',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
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


app.controller('eventController', eventFunction);

function eventFunction($scope, eventResource, accountResource, eventBackResource,
  eventVoluntaryResource, $routeParams) {
  function getEvent(){
    eventResource.get({ id : $routeParams.id }, function(data){
      $scope.event=data;
      getEventBack();
      getEventVoluntary();
    });
  };
  getEvent();

  function getEventBack(){
    eventBackResource.query({ event : $routeParams.id}, function(data){
      $scope.eventBacks = data[0];
    });
  };

  function getEventVoluntary(){
    eventVoluntaryResource.query({ event : $routeParams.id}, function(data){
      $scope.eventVoluntary = data;
    });
  };
};
