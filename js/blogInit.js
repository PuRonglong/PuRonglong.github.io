if (!debug) {
	requirejs.config({
		baseUrl: 'js',
		paths: {
			jquery: 'lib/jquery',
			angular: 'lib/angular',
			ngRoute: 'lib/angular-ui-router',
			ngAnimate: 'lib/angular-animate',
			require: 'lib/require',
			bootstrap: 'lib/bootstrap',
			markdown: 'lib/markdown',
			hljs: 'lib/highlight.pack',
			blogApp: 'blogApp',
			blogController: 'blogController',
			blogDirective: 'blogDirective',
			blogFilter: 'blogFilter'
		},
		shim: {
			"angular": {
				exports: "angular"
			},
			"ngRoute": {
				deps: ['angular'],
				exports: "ngRoute"
			},
			"ngAnimate": {
				deps: ['angular'],
				exports: "ngAnimate"
			},
			"bootstrap": {
				deps: ['jquery'],
				exports: "bootstrap"
			},
			"markdown": {
				exports: "markdown"
			}
		}
	});
}else {
	requirejs.config({
		baseUrl: 'js',
		paths: {
			jquery: '//cdn.bootcss.com/jquery/2.2.0/jquery.min',
			angular: '//cdn.bootcss.com/angular.js/1.3.20/angular.min',
			ngRoute: '//cdn.bootcss.com/angular-ui-router/0.2.18/angular-ui-router.min',
			ngAnimate: '//cdn.bootcss.com/angular.js/1.3.20/angular-animate.min',
			require: '//cdn.bootcss.com/require.js/2.1.22/require.min',
			bootstrap: '//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min',
			markdown: 'lib/markdown',
			hljs: 'lib/highlight.pack',
			blogApp: 'blogApp',
			blogController: 'blogController',
			blogDirective: 'blogDirective',
			blogFilter: 'blogFilter'
		},
		shim: {
			"angular": {
				exports: "angular"
			},
			"ngRoute": {
				deps: ['angular'],
				exports: "ngRoute"
			},
			"ngAnimate": {
				deps: ['angular'],
				exports: "ngAnimate"
			},
			"bootstrap": {
				deps: ['jquery'],
				exports: "bootstrap"
			},
			"markdown": {
				exports: "markdown"
			}
		}
	});
}

var libs = ['jquery', 'angular', 'ngRoute', 'ngAnimate', 'require', 'bootstrap', 'markdown', 'hljs', 'blogApp',
'blogController', 'blogDirective', 'blogFilter'];

require(libs, function($, angular){
	return	angular.bootstrap(document, ["puronglong"]);
});