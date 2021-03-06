module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  grunt.initConfig({
    sass: {
      compile: {
        files: {
          '../../css/app.css': '../../css/app.sass'
        }
      }
    },
    concat: {
      css: {
        src: [
        '../../css/app.css'
        ],
        dest: '../../dist/app.css'
      },
      libjs: {
        src: [
          'bower_components/react/react.js',
          'bower_components/react/react-dom.js',
          'bower_components/babel/browser.js',
          'bower_components/jquery/dist/jquery.js',
          'bower_components/remarkable/dist/remarkable.js',
        ],
        dest: '../../dist/vendor.js'
      },
      appjs: {
        src: [
          'app.js',
          'apps/*.js',
          'apps/**/*.js',
        ],
        dest: '../../dist/app.js'
      }
    },
    cssmin: {
      options: {
        shorthandandCompacting: false,
        roundingPrecision: -1
      },
      target: {
        files: {
          '../../dist/app.min.css': [
            '../../dist/app.css'
          ]
        }
      }
    },
    uglify: {
      js: {
        files: {
          '../../dist/app.min.js': [
            '../../dist/vendor.js',
            '../../dist/app.js'
          ]
        }
      }
    }
  });

  grunt.registerTask('minify', [
    'sass',
    'concat',
    'cssmin',
    'uglify'
  ]);


};