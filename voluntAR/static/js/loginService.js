'use strict';

angular.module('app').factory('loginService', loginService);

function loginService($http, $location, localStorageService, toaster) {
  return {
    login : login
  };

  function login() {
    var data_login = localStorageService.get('data_login');

    $http.post('http://localhost:8000/auth/login/', data_login).then(function(result){

      // obtengo token de auth
      $http.defaults.headers.common.Authorization = 'Token ' + result.data.auth_token;

      // obtengo datos del usuario y los guardo en un storage local
      $http.get('http://localhost:8000/auth/me/').then(function(user){
        localStorageService.set('user', user);
      });

      // redirigo la ruta
      return $location.path( "/" );
    }, function() {
    	// login erroneo , muestra error
      return toaster.pop({
        type: 'error',
        title: 'Error',
        body: 'Los datos ingresados son incorrectos.',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
      });
    });
  }
}