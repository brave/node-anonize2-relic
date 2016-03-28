var mkdir = require('fs').mkdir;
var platform = require('os').platform();
var spawn = require('child_process').spawn;
  
var configure = { darwin : [ '-DOPSYS=MACOS', '-DSTLIB=ON', '-DSHLIB=OFF', '-DALLOC=AUTO', '-DBENCH=0', '-DTESTS=0' ],
                  linux  : [ '-DOPSYS=LINUX' ]
                }[platform];
if (!configure) {
  console.log('unsupported platform: ' + platform);
  process.exit(1);
}

var args = [ '../relic', '-G', 'Unix Makefiles',
             '-DCHECK=on', '-DDEBUG=on', '-DARCH=X64', '-DALIGN=16', '-DCOLOR=OFF', '-DSEED=UDEV',
             '-DWITH=BN;DV;FP;FPX;EP;EPX;PP;MD', '-DBN_PRECI=256', '-DBN_MAGNI=DOUBLE'
           ].concat(configure);


var target = './anonize2/relic-build';

mkdir(target, parseInt('755', 8), function (err) {
  var out;
  var println = function (more) { out = Buffer.concat([ out, more ]); };

  var loser = function (s, err) {
    console.log(s);
    console.log(err.toString());
    console.log(out.toString());
    process.exit(1);
  };

  if ((err) && (err.code !== 'EEXIST')) throw err;

  out = new Buffer(0);
  var cmake = spawn('cmake', args, { cwd: target }).on('error', function (err) {
    loser('cmake failed', err);
  }).on('close', function (code) {
    if (code) process.exit(code);

    out = new Buffer(0);     
    var make = spawn('make', [], { cwd: target }).on('error', function (err) {
      loser('make failed', err);
    }).on('close', process.exit);

    make.stdout.on('data', function (more) { console.log(more.toString().trim()); });
    make.stderr.on('data', println);
  });

  cmake.stdout.on('data', println);
  cmake.stderr.on('data', println);
});
