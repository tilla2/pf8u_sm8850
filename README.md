# OPPO/OnePlus/Realme SM8850/MT6993 Series Universal 6.12 Kernel Automated Build Script
[![STAR](https://img.shields.io/github/stars/cctv18/oppo_oplus_realme_sm8850?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU%2BR2l0SHViPC90aXRsZT48cGF0aCBkPSJNMTIgLjI5N2MtNi42MyAwLTEyIDUuMzczLTEyIDEyIDAgNS4zMDMgMy40MzggOS44IDguMjA1IDExLjM4NS42LjExMy44Mi0uMjU4LjgyLS41NzcgMC0uMjg1LS4wMS0xLjA0LS4wMTUtMi4wNC0zLjMzOC43MjQtNC4wNDItMS42MS00LjA0Mi0xLjYxQzQuNDIyIDE4LjA3IDMuNjMzIDE3LjcgMy42MzMgMTcuN2MtMS4wODctLjc0NC4wODQtLjcyOS4wODQtLjcyOSAxLjIwNS4wODQgMS44MzggMS4yMzYgMS44MzggMS4yMzYgMS4wNyAxLjgzNSAyLjgwOSAxLjMwNSAzLjQ5NS45OTguMTA4LS43NzYuNDE3LTEuMzA1Ljc2LTEuNjA1LTIuNjY1LS4zLTUuNDY2LTEuMzMyLTUuNDY2LTUuOTMgMC0xLjMxLjQ2NS0yLjM4IDEuMjM1LTMuMjItLjEzNS0uMzAzLS41NC0xLjUyMy4xMDUtMy4xNzYgMCAwIDEuMDA1LS4zMjIgMy4zIDEuMjMuOTYtLjI2NyAxLjk4LS4zOTkgMy0uNDA1IDEuMDIuMDA2IDIuMDQuMTM4IDMgLjQwNSAyLjI4LTEuNTUyIDMuMjg1LTEuMjMgMy4yODUtMS4yMy42NDUgMS42NTMuMjQgMi44NzMuMTIgMy4xNzYuNzY1Ljg0IDEuMjMgMS45MSAxLjIzIDMuMjIgMCA0LjYxLTIuODA1IDUuNjI1LTUuNDc1IDUuOTIuNDIuMzYuODEgMS4wOTYuODEgMi4yMiAwIDEuNjA2LS4wMTUgMi44OTYtLjAxNSAzLjI4NiAwIC4zMTUuMjEuNjkuODI1LjU3QzIwLjU2NSAyMi4wOTIgMjQgMTcuNTkyIDI0IDEyLjI5N2MwLTYuNjI3LTUuMzczLTEyLTEyLTEyIiBmaWxsPSIjZmZmZmZmIj48L3BhdGg%2BPC9zdmc%2B)](https://github.com/cctv18/oppo_oplus_realme_sm8850/stargazers)
[![FORK](https://img.shields.io/github/forks/cctv18/oppo_oplus_realme_sm8850?style=flat&logo=greasyfork&color=%2394E61A)](https://github.com/cctv18/oppo_oplus_realme_sm8850/forks)
[![COOLAPK](https://img.shields.io/badge/cctv18_2-cctv18_2?style=flat&logo=android&logoColor=FF4500&label=Coolapk&color=FF4500)](http://www.coolapk.com/u/22650293)
[![DISCUSSION](https://img.shields.io/badge/Discussions-discussions?logo=livechat&logoColor=FFBBFF&color=3399ff)](https://github.com/cctv18/oppo_oplus_realme_sm8850/discussions)

<img alt="Endpoint Badge" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcctv18%2Fkernel-workshop%2Frefs%2Fheads%2Fhotfix%2Fnotice.json">

##### 
A more convenient and fast automated universal 6.12 kernel build script for OPPO/OnePlus/Realme series devices with Snapdragon 8 Elite Gen5 (SM8850)/Dimensity 9500 (MT6993).
##### 
The original intention of this project is to solve the following issues:
- The official manufacturer has been slacking off, open-sourcing only half of the code, which prevents some kernel code from compiling properly via existing configuration XMLs, or even lacks compilation configuration XMLs entirely;
- Due to the introduction of numerous new mechanisms in the 6.12 kernel, including Rust code, the conventional method of compiling kernels using make commands can no longer complete the build successfully. It forces reliance on the inefficient Bazel build system, while the official Bazel compiler is overly unstable and bloated, prone to various inexplicable errors with almost no effective solutions available online, making it extremely unfriendly for beginners;
- Existing common compilation workflows for 6.12 kernels (using Bazel/pulling third-party toolchains) are extremely slow. Even with caching, subsequent builds often take 20-30 minutes, and Bazel is incompatible with ccache, failing to save compilation caches properly.
## Main Content of This Project (and Plans)
- Compiles using official AOSP LLVM/Clang 19 + Rust v1.82.0, excludes unnecessary vendor source code from the official sources, significantly optimizes the build process, and introduces a ccache caching mechanism. Compared to the original Bazel compiler, this reduces build time by nearly 2/3 (the original official compiler typically takes over 1 hour per build), improves build stability, and outputs logs that are easier to maintain and debug;
- Fixes bugs/outdated patches in the official code and introduces numerous third-party updates/feature support;
- Provides dual versions of scripts: GitHub Actions online build / local shell build.
## Implemented:
- [x] Universal OKI kernel for OPPO/OnePlus/Realme Snapdragon SM8850 (based on OnePlus 15 source 6.12.23 / OnePlus Ace 6T source 6.12.38; other models with the same kernel version but not SM8850 can be tested independently, with some being fully compatible)
- [x] Universal OKI kernel for OPPO/OnePlus/Realme Dimensity MT6993 (based on OPPO Find X9 source 6.12.23; other models with the same kernel version but not MT6993 can be tested independently, with some being fully compatible)
- [x] Multiple KSU versions selectable: ReSukiSU/SukiSU Ultra/KernelSU Next/Original KernelSU
- [x] Introduced exclusively designed [ccache-ECS](https://github.com/cctv18/ccache-ECS) caching and extensive build process optimizations, stabilizing build times at approximately 6 minutes *(the first build will pull a public preset ccache; from the second build onwards, assuming no major configuration changes, single build time is ~6 mins; if unused for two weeks since last invocation, the cache is automatically cleared, triggering an automatic cache rebuild on next build)*
- [x] Introduced O2 compilation optimization to improve kernel runtime performance
- [x] lz4 1.10.0 & zstd 1.5.7 algorithm update & optimization patches (from [@ferstar](https://github.com/ferstar), ported by [@Xiaomichael](https://github.com/Xiaomichael), 6.12 version patch remade by [@cctv18](https://github.com/cctv18))
- [x] Ported lz4kd support to 6.12 kernel (optional patch)
- [x] Optional inclusion of BBR/Brutal and a series of TCP congestion control algorithms
- [x] [ADIOS IO Scheduler](https://github.com/firelzrd/adios) port
- [x] Added network connection performance optimization configuration options (to provide support for ipset and programs requiring advanced network features like iptables)
- [x] Droidspaces containerization support (a complete Linux environment container implementation that is lighter than traditional Docker/LXC and easier to port)
- [x] Added support for [Mountify](https://github.com/backslashxx/mountify) module
- [x] Added Re:Kernel support, working with Freezer, NoActive, etc., to reduce power consumption
- [x] Added [Kernel Baseband Wipe Protection (By @showdo)](https://github.com/vc-teahouse/Baseband-guard), effectively preventing malicious wipe scripts/programs from damaging system partition data
## To Be Implemented:
- [ ] Built-in zram, eliminating the need to mount external zram.ko ~~(With the new lz4 & zstd patches, is this really still necessary?)~~
- [ ] Nethunter wireless card monitor mode support
- [ ] kexec kernel hot-switching support
- More optimizations and feature ports...
- More optimizations and feature ports...
##### 
##### 
##### 
## Acknowledgments
- WildKernel's OnePlus series kernel build script: [WildKernels/OnePlus_KernelSU_SUSFS](https://github.com/WildKernels/OnePlus_KernelSU_SUSFS)
- ReSukiSU: [ReSukiSU/ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)
- SukiSU Ultra: [SukiSU-Ultra/SukiSU-Ultra](https://github.com/SukiSU-Ultra/SukiSU-Ultra)
- susfs4ksu: [ShirkNeko/susfs4ksu](https://github.com/ShirkNeko/susfs4ksu)
- ReSukiSU: [ReSukiSU/ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)
- pershoot's maintained KernelSU Next repository: [pershoot/KernelSU-Next](https://github.com/pershoot/KernelSU-Next)
- Original KernelSU: [tiann/KernelSU](https://github.com/tiann/KernelSU)
- Kernel Baseband Wipe Protection Module: [vc-teahouse/Baseband-guard](https://github.com/vc-teahouse/Baseband-guard)
- KSUN's multi-manager patches: [WildKernels/kernel_patches](https://github.com/WildKernels/kernel_patches)
- ~~Localized kernel build script (defunct): [Suxiaoqinx/kernel_manifest_OnePlus_Sukisu_Ultra](https://github.com/Suxiaoqinx/kernel_manifest_OnePlus_Sukisu_Ultra)~~

<!-- This is a visitor counter to see how many people have visited my project homepage -->
<div align="center">
  <img width="0" height="0" src="https://count.getloli.com/get/@:cctv18" />
</div>