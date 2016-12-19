/*!
 * author: puronglong
 */

 /*当页面加载完之后执行*/
window.onload = function(){
	// $('#loading').css('display', 'none');
	$('#loading').fadeOut();
	$('.slider').slider({
		full_width: true,
		indicators: true,  // 导航标识
		interval: 8000,   // 间隔时间设置
		transition: 700    // 持续时间设置
	});

	$('.button-previous-left').on('click', function () {
		$('.slider').slider('prev');
	});

	$('.button-previous-right').on('click', function () {
		$('.slider').slider('next');
	});
	$('#menu').addClass('menu animated bounceInDown');
	
};
