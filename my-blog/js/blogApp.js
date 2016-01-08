define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong', ['ui.router', 'ngAnimate']);//定义了一个模块,后面是依赖列表

	puronglong.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
		$stateProvider
			.state('main', {
				url: '/',
				templateUrl: './template/blog-main.html'
			})
			.state('home', {
				url: '',
				templateUrl: './template/blog-main.html'
			})
			.state('blogList', {
				url: '/blogList',
				templateUrl: './template/blog-list.html'
			});

		$urlRouterProvider
			.when("", "/");
	}]);
})