# node-gphoto2
A Node.js wrapper for [libgphoto2](http://www.gphoto.org). Useful for remote controlling of DSLRs and other digital cameras supported by [gphoto2](http://www.gphoto.org).


The included test application currently allows you to

* receive a live preview of your camera (if supported). Tested with an EOS 550D on a 2010 iMac at ~17 fps using Chrome (Safari doesn't work and FF is slow as hell).
* query a list of available configuration options
* query the values of specific configuration options

The test suite can be run using ``npm test``. There's also a small test application in test/test-server.coffee which runs on http://localhost:1337 and allows to change camera settings and to
take pictures.

## Prerequisites
* Node.js ~0.10.0
* NPM ~1.2.15
* libgphoto2 ~2.5.0 - via ``brew install libgphoto2``, ``apt-get install libgphoto2-2-dev`` or download and build from http://www.gphoto.org/proj/libgphoto2/
* pkg-config | dpkg (used for dependency checking)
* clang compiler

## Test/dev prerequisites
* async
* coffee-script
* mocha
* should
* sinon

## Test-server prerequisites
* express
* jade
* underscore

## Installation
After installing the dependencies, just install using:
    npm install gphoto2
If it fails, please thoroughly check the output - link errors usually indicate missing dependencies.
Also, the script tries to detect wether libgphoto2 is correctly installed - if this check fails although you properly installed it, please report :)

## Usage
This example only shows how to achieve certain tasks, it's not meant to be executed without any asynchronous control flow logic.

```javascript
gphoto2 = require('gphoto2');
GPhoto = new gphoto2.GPhoto2();
fs = require('fs');

// List cameras / assign list item to variable to use below options
GPhoto.list(function(list){
  if(list.length === 0) return;
  var camera = list[0];
  console.log("Found", camera.model);

  // get configuration tree
  camera.getConfig(function(er, settings){
    console.log(settings);
  });

  // Set configuration values
  camera.setConfigValue('capturetarget', 1, function(er){
    //...
  })

  // Take picture with camera object obtained from list()
  camera.takePicture({download:true}, function(er, data){
    fs.writeFile("picture.jpg", data);
  });

  // Take picture without downloading immediately
  camera.takePicture({download:false}, function(er, path){
    console.log(path);
  });

  // Take picture and download it to filesystem
  camera.takePicture({
      download:true,
      targetPath:'/tmp/foo.XXXXX'
    }, function(er, tmpname){
      fs.rename(tmpname, './picture.jpg');
  });

  // Download a picture from camera
  camera.downloadPicture({
      cameraPath:'/store_00020001/DCIM/100CANON/IMG_1231.JPG',
      targetPath:'/tmp/foo.XXXXX'
    }, function(er, tmpname){
      fs.rename(tmpname, './picture.jpg');
  });

  // Get preview picture (from AF Sensor, fails silently if unsupported)
  camera.takePicture({preview:true}, function(er, data){
    fs.writeFile("picture.jpg", data);
  });
});
```

## Versioning

This project uses [Semantic versioning](https://github.com/mojombo/semver).


## Contributors

* [Leonhardt Wille](https://github.com/lwille)
* [david noelte](https://github.com/marvin)
* [Michael Kötter](https://github.com/michaelkoetter)

