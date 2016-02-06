define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong', ['ui.router', 'ngAnimate']);//定义了一个模块,后面是依赖列表

	puronglong.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider){
		$stateProvider
			.state('main', {
				url: '/',
				templateUrl: './template/blog-index.html'
			})
			.state('index', {
				url: '',
				templateUrl: './template/blog-index.html'
			})
			.state('blog',{
				url: '/blog',
				templateUrl: './template/blog-common.html'
			})
			.state('blog.blogListItem', {
				url: '/:type',
				templateUrl: './template/blog-list.html',
				controller: 'blogListItem'
			})
			.state('blog.blogContent', {
				url: '/post/:article',
				templateUrl: './template/blog-content.html',
				controller: 'blogListContent'
			});

		$urlRouterProvider
			.when("", "/");
	}]);
});