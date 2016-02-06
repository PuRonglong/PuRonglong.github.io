define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong');

	return puronglong.filter('blogListType', function(){
		return function (data, type){
			console.log(type);
			var typeList = [], i, len;

			if(data && type && type !== 'all'){
				for (i = 0, len = data.length; i < len; i++){
					var eachData = data[i];
					if (eachData.type === type){
						typeList.push(eachData);
					}
				}
				return typeList;
			}
			return data;
		}
	})
});