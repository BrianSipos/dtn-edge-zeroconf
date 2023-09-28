# Lightweight Bundle Protocol Edge Node with Zero-Configuration and Zero-State

The internet-draft is hosted at [draft-sipos-dtn-edge-zeroconf](https://datatracker.ietf.org/doc/draft-sipos-dtn-edge-zeroconf/).

A local build of the current main branch is available [draft-sipos-dtn-edge-zeroconf.html](https://briansipos.github.io/dtn-edge-zeroconf/draft-sipos-dtn-edge-zeroconf.html) with its [misspelling.txt](https://briansipos.github.io/dtn-edge-zeroconf/misspelling.txt).

Prerequisites to building can be installed on Ubuntu with:
```
sudo apt-get install -y cmake xml2rfc xmlstarlet aspell python3
```
and then the document can be built with
```
cmake -S . -B build
cmake --build build
```
