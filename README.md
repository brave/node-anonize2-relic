# node-anonize2-relic
Node bindings to the [anonize2](https://gitlab.com/abhvious/anonize2) library,
using the [RELIC toolkit](https://github.com/relic-toolkit/relic).

## Licensing
This repository contains the [anonize2](https://gitlab.com/abhvious/anonize2) library,
which is licensed under [Apache v2.0 License](https://gitlab.com/abhvious/anonize2/blob/master/LICENSE.txt).
This repository also contains code derived from the [RELIC toolkit](https://github.com/relic-toolkit/relic),
which is available under a [modified LGPL](https://github.com/relic-toolkit/relic/blob/master/COPYING) license.
All other files are licensed under the [MPL-2.0](./LICENSE).

The RELIC toolkit license is LGPLv2.1 with these overriding provisions:

   1. Making modifications to RELIC configuration files, build scripts and
      configuration headers such as "relic_conf.h" in order to create a
      customized build setup of RELIC with the otherwise unmodified source code,
      does not constitute a derived work.

   2. Statically linking the RELIC library into a user application does not
      make the user application a derived work, and therefore does not require
      the user to distribute the source code or object code of their own
      application. The RELIC source code with all modifications must still be
      passed on in the same way as using RELIC as a shared library.

   3. Using source code obfuscation on the RELIC source code when distributing
      it is not permitted.

It is the intent of this package to produce a `librelic_s.a`,
which is then used by as an add-on for node.js,
it is believed that this package fully complies with the RELIC toolkit's licensing requirements.

## You must have CMake installed
To build this package properly,
you **must** have [CMake](https://cmake.org/) installed along with _make_.
The `preflight.js` script invoked during `npm install` will invoke CMake as appropriate,
and then run make.
This takes place before the usual `node-gyp` magic.

The maintainers understand that this setup breaks a lot of rules for portable packages;
if you have a better way,
please let us know.
Until then: [_mea culpa, mea culpa, mea máxima culpa_](https://en.wikipedia.org/wiki/Mea_culpa).
