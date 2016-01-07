define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong', ['ui.router', 'ngAnimate']);//定义了一个模块,后面是依赖列表

	puronglong.config(['$stateProvider', function($stateProvider){
		$stateProvider
			.state('main', {
				url: '/',
				templateUrl: './template/blog-main.html'
			})
			.state('home', {
				url: '',
				templateUrl: './template/blog-main.html'
			})
			.state('list', {
				url: '/list',
				templateUrl: './template/blog-list.html'
			})
	}]);
})