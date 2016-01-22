define(['jquery', 'angular'], function($, angular){
	var puronglong = angular.module('puronglong');

	puronglong.controller('blogListItem', function($scope, $http, $stateParams){
		$http.get('./post/list.md').success(function(data){
			return $scope.bloglist = eachList(data);
		});
	});

	//返回包含所有list的数组
	eachList = function(data){
		var list = [], eachListDetail;
		data = data.split(/\n[\-=]+/);
		data.forEach(function(eachData){
			eachListDetail = listDetail(eachData);
			if(eachListDetail.hide !== 'true'){
				list.push(eachListDetail);
			}
		});

		return list;
	};

	//返回每一个list的详细信息
	listDetail = function(data){
		var list = {
			title: '',
			disc: '',
			type: '',
			url: '',
			hide: '',
			tag: ''
		};
		var allLine = data.split('\n');
		var i, eachLine, eachLineAttr, key, value;
		for (i = 0; i < allLine.length; i++){
			eachLine = allLine[i];
			eachLineAttr = eachLine.split(':');
			key = $.trim(eachLineAttr[0]), value = $.trim(eachLineAttr[1]);
			if (list.hasOwnProperty(key)){
				list[key] = value;
				console.log(list[key] + ":" + value);
			}
		}
		list.date = list.url.split('-');
		list.year = parseInt(list.date[0], 10);
		list.month = parseInt(list.date[1], 10);
		list.day = parseInt(list.date[2], 10);

		return list;
	};

	listType = function(data){
		var allType;
		allType = listDetail(data).type;
	};
});