var gulp = require('gulp');
var minifyCss = require('gulp-minify-css');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');

gulp.task('styleCss', function(){
	return gulp.src('./css/style.css')
		.pipe(minifyCss())
		.pipe(rename('style.min.css'))
		.pipe(gulp.dest('./css/lib'));
});

gulp.task('blogStyleCss', ['styleCss']);




gulp.task('requirejs', function () {
	return gulp.src(['./js/lib/require.js'])
			.pipe(uglify())
			.pipe(rename('require.min.js'))
			.pipe(gulp.dest('./js/lib'));
});

gulp.task('requirejsLib', ['requirejs']);