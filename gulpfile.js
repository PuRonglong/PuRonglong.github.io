var gulp = require('gulp');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');

gulp.task('styleCss', function(){
	return gulp.src('./css/style.css')
		.pipe(minifyCss())
		.pipe(rename('style.min.css'))
		.pipe(gulp.dest('./css/lib'));
});

gulp.task('blogStyleCss', ['styleCss']);