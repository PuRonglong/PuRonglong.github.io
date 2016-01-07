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
			highLight: 'lib/highlight.pack',
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
			"markdown": {
				exports: "markdown"
			}
		}
	});
}

var libs = ['jquery', 'angular', 'ngRoute', 'ngAnimate', 'require', 'bootstrap', 'markdown', 'highLight', 'blogApp',
'blogController', 'blogDirective', 'blogFilter'];

require(libs, function($, angular){
	alert('a');
	return	angular.bootstrap(document, ["puronglong"]);
});