define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong');

	puronglong.directive('markdown', function(){
		return {
			restrict: 'A',
			scope: {
				content: '=markdownText'
			},
			link: function(scope, element, attrs){
				var cssUrl, link, loading, them;
				them = attrs.theme ? attrs.theme : 'zenburn';
				cssUrl = require.toUrl('../css/' + them + '.css');
				link = document.createElement('link');
				link.type = 'text/css';
				link.rel = 'stylesheet';
				link.href = cssUrl;
				document.getElementsByTagName('head')[0].appendChild(link);
				return require(['markdown', 'hljs'], function(md, hljs){
					scope.$watch(function(){
						return scope.content;
					}, function(newValue){
						if (newValue){
							element.html(md.toHTML(newValue));
							return $(element).find('pre>code').each(function(i, block){
								return hljs.highlightBlock(block);
							});
						}
					});
					if (scope.content) {
						element.html(md.toHTML(scope.content));
						return $(element).find('pre>code').each(function(i, block) {
							return hljs.highlightBlock(block);
						});
					}
				})
			}
		}
	})
});