define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong');

	return puronglong.filter('blogListType', function(){
		return function (data, type){
			console.log(data);
			var typeList = [], i;
			var len = data.length;
				for (i = 0; i < len; i++){
					var eachData = data[i];
					if (eachData.type === type){
						return typeList.push(eachData);
					}
				}
				return typeList;
		}
	})
});