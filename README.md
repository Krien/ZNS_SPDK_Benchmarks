# ZNS_SPDK_Benchmarks
This repository contains the results of various benchmarks of various ZNS experiments.
It also contains some benchmarks itself. It contains benchmarks for I/O storage engines and applications on top of ZNS.

## SPDK
The SPDK directory contains benchmarks for ZNS operations when using SPDK.
It also contains plotting tools and some some general results that these benchmarks can return.

## TropoDB
The TropoDB directory contains benchmarks results for the key-value store [TropoDB](https://github.com/Krien/TropoDB/).
The results were generated with the benchmarks defined in [zns_tests](https://github.com/Krien/TropoDB/tree/master/implementation/rocksdb/zns_tests).
It also comes with some general plotting tools.
