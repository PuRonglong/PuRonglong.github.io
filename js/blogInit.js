if (debug) {
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

	});
}

var libs = ['jquery', 'angular', 'ngRoute', 'ngAnimate', 'require', 'bootstrap', 'markdown', 'hljs', 'blogApp',
'blogController', 'blogDirective', 'blogFilter'];

require(libs, function($, angular){
	return	angular.bootstrap(document, ["puronglong"]);
});