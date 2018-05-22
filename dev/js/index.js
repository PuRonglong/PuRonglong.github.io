$(document).ready(function(){
    var nav = $('.g-nav');

    /**
     * Responsive Navigation
     */
    $('#menu-toggle').on('click', function(e) {
        var duration = 200;
        nav.slideToggle(duration);
        $(document).on('click', function() {
            nav.slideUp(duration);
        });
        e.stopPropagation();
    });

    nav.on('click', function(e) {
        e.stopPropagation();
    });

    /*
    *  Header Bar
    */
    if($(window).width() > 695) {
        var header = $('.g-header');
        var headerHeight = header.outerHeight();
        var logo = $('.g-logo');
        var navText = nav.find('a');
        var themeStyle = $('.g-banner').attr('data-theme');
        var scFlag = $(document).scrollTop();

        $(document).scroll(function() {
            var scrollTop = $(this).scrollTop();
            var navClassName = 'nav-' + themeStyle;

            if (scrollTop > headerHeight) {
                if(scrollTop > 3 * headerHeight) {
                    header.addClass('headerUp');
                }
                header.css({
                    'background-color': 'rgba(255, 255, 255, .98)',
                    'box-shadow': '0 1px 12px rgba(0, 0, 0, .08)'
                });
                logo.css({
                    'background-size': '100% 100%'
                });
                navText.css('color', '#666');
                nav.addClass(navClassName);
            } else {
                header.removeClass('headerUp');
                header.css({
                    'background-color': 'transparent',
                    'box-shadow': 'none'
                });
                logo.css({
                    'background-size': '100% 100%'
                });
                navText.css('color', '#fff');
                nav.removeClass(navClassName);
            }

            // scroll action
            if (scFlag > scrollTop) {
                header.addClass('headerDown');
            } else {
                header.removeClass('headerDown');
            }
            scFlag = scrollTop;
        });
    }

    /*
    * Post Cover Resize
    */
    function postCover(img, container) {
        var imgWidth = img.width();
        var containerWidth = container.width();
        var imgHeight = img.height();
        var containerHeight = container.height();

        if (imgHeight < containerHeight) {
            img.css({
                'width': 'auto',
                'height': '100%'
            });
            imgWidth = img.width(),
            containerWidth = container.width();
            var marginLeft = (imgWidth - containerWidth) / 2;
            img.css('margin-left', '-' + marginLeft + 'px');
        } else {
            var marginTop = (containerHeight - imgHeight) / 2;
            img.css('margin-top', marginTop + 'px');
        }

        img.fadeIn();
    }

    /**
     * The Post Navigator
     */
    $('.read-next-item section').each(function() {
        var n = $(this).height();
        var rn = $('.read-next-item').height();
        $(this).css('margin-top', (rn - n) / 2 + 'px');
        $(this).fadeIn();
    });

    $('.read-next-item img').each(function(){
        postCover($(this), $('.read-next-item'));
    });

    /**
     * Pagination
     */
    function pagination() {
        var total = parseInt($('#total_pages').val());
        var current = parseInt($('#current_pages').val());
        var baseUrl = $('#base_url').val();
        var limit = 3;

        var link_html = '';

        for (var i = current - limit; i < current; i++) {
            if (i > 0 && i !== 1) {
                link_html += '<a href="' + baseUrl + 'page' + i + '" class="page-link page-num">' + i + '</a>';
            } else if (i === 1) {
                link_html += '<a href="' + baseUrl + '" class="page-link page-num">' + i + '</a>';
            }
        }

        link_html += '<span class="page-link page-num active">' + current + '</span>';

        for (var j = current + 1; j <= current + limit; j++) {
            if (j <= total) {
                link_html += '<a href="' + baseUrl + 'page' + j + '" class="page-link page-num">' + j + '</a>';
            }
        }

        $('#page-link-container').html(link_html);
    }
    pagination();

    /**
     * Search
     */
    function Search() {
        var self = this;
        var input = $('#search_input');
        var result = $('.search_result');

        input.focus(function() {
            $('.icon-search').css('color', '#3199DB');
            result.show();
        });

        input.keyup(debounce(this.autoComplete));

        $(document).click(function(e) {
            if(e.target.id === 'search_input' || e.target.className === 'search_result' || e.target.className === 'search_item') {
                return;
            }
            $('.icon-search').css('color', '#CAD3DC');
            result.hide();
        });
    }

    Search.prototype.autoComplete = function() {
        var keywords = this.value.toLowerCase();

        if (keywords.length) {
            $('.icon-search').css('color', '#3199DB');
        } else {
            $('.icon-search').css('color', '#CAD3DC');
        }

        $.getJSON('../../search.json').done(function(data) {
            var html = '';
            for (var i in data) {
                var item = data[i];
                var title = item.title;
                var tags = item.tags;
                var url = item.url;

                var k = title + tags;
                if (keywords !== '' && k.toLowerCase().indexOf(keywords) >= 0) {
                    html += '<a class="search_item" href="' + item.url + '">' + item.title + '</a>';
                }
            }
            $('.search_result').html(html);
        });
    };

    function debounce(fn, delay) {
        var timer;
        delay = delay || 120;

        return function () {
            var ctx = this;
            var args = arguments;
            var later = function() {
                fn.apply(ctx, args);
            };
            clearTimeout(timer);
            timer = setTimeout(later, delay);
        };
    }

    new Search();

    /**
     * Night mode
     */
    function nightMode() {
        var el = $('body');
        var className = 'night-mode';

        var date = new Date();
        var hour = date.getHours();

        if ((hour >= 0 && hour <= 6) || hour === 23) {
            el.addClass(className);
        }
    }

    if ($('#nm-switch').val() === 'true') {
        nightMode();
    }

    /**
     * Copy and copyright
     */
    function setClipboardData(str) {
        str += '\n\n著作权归作者所有。\n商业转载请联系作者获得授权,非商业转载请注明出处。\n原文: ' + location.href;
        $('.post-content').on('copy', function(e) {
            var data = window.clipboardData || e.originalEvent.clipboardData;
            data.setData('text/plain', str);
            e.preventDefault();
        });
    }
    $('.post-content').on('mouseup', function(e) {
        var txt = window.getSelection();
        if (txt.toString().length >= 30) {
            setClipboardData(txt);
        }
    });

    //图片延迟加载
var num = document.getElementsByTagName('img').length;
var img = document.getElementsByTagName("img");
var n = 0; //存储图片加载到的位置，避免每次都从第一张图片开始遍历
lazyload(); //页面载入完毕加载可视区域内的图片
window.onscroll = lazyload;
function lazyload() { //监听页面滚动事件
    var seeHeight = document.documentElement.clientHeight; //可见区域高度
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop; //滚动条距离顶部高度
    for (var i = n; i < num; i++) {
    	//如果图片距离顶部的高度小于可见区域高度加上滚动的高度
        if (img[i].offsetTop-300 < seeHeight + scrollTop) {
            if (img[i].getAttribute("src") == "") {
                img[i].src = img[i].getAttribute("data-src");
            }
            n = i + 1;
        }else{
            
        }
    }
}

});