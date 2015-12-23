var gulp = require('gulp');

// define plug-ins
var flatten = require('gulp-flatten');
var gulpFilter = require('gulp-filter');
var concat = require('gulp-concat');

// Define paths variables
var dest_path =  'static';
// grab libraries files from bower_components, minify and push in /public
gulp.task('all', ['js', 'css', 'fonts']);

gulp.task('js', function () {
        var jsFilter = gulpFilter('**/*.min.js');
        gulp.src('./bower_components/**')
        .pipe(jsFilter)
        .pipe(concat('app.min.js'))
        .pipe(gulp.dest(dest_path + '/js'));
});

gulp.task('css', function () {
        var jsFilter = gulpFilter('**/*.min.css');
        gulp.src('./bower_components/**')
        .pipe(jsFilter)
        .pipe(concat('app.min.css'))
        .pipe(gulp.dest(dest_path + '/css'));
});

gulp.task('fonts', function() {
        var fontFilter = gulpFilter(['**/*.eot', '**/*.woff', '**/*.svg', '**/*.ttf']);
        return gulp.src('./bower_components/**')
        .pipe(fontFilter)
        .pipe(flatten())
        .pipe(gulp.dest(dest_path + '/fonts'));
});
