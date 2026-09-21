# gnPOA: GPU-Accelerated Sequence-to-Graph Partial Order Alignment

<p align="center">
  <img src="https://img.shields.io/badge/CUDA-11.x%20%7C%2012.x-76B900.svg?logo=nvidia" alt="CUDA">
  <img src="https://img.shields.io/badge/Language-C%20%2F%20CUDA%20C%2B%2B-blue.svg" alt="Language">
  <img src="https://img.shields.io/badge/Platform-Linux%20(x86__64)-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

**gnPOA** is a high-throughput, GPU-accelerated partial order alignment engine designed for **sequence-to-graph mapping**. By redesigning the graph representation into memory-efficient flattened arrays on the GPU and implementing **on-device dynamic programming (DP) and traceback**, gnPOA delivers high-speed alignment while rigorously preserving alignment score accuracy under complex convex double-affine gap models.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0509c1a4-c52e-4c06-a9fe-6277e723bd95" alt="gnPOA Architecture" width="800"/>
  <br>
  <em>Figure: Overview of gnPOA GPU-accelerated sequence-to-graph alignment workflow.</em>
</p>

---

## ✨ Key Features

- ⚡ **End-to-End GPU Execution**: Both dynamic programming scoring and traceback are performed entirely on the GPU. Only compact CIGAR strings and final scores are transferred back to the host, eliminating PCIe bandwidth bottlenecks.
- 🧬 **Convex Double-Affine Gap Scoring**: Explicitly maintains all six DP matrices (`M, E1, E2, F1, F2, H`) to accurately model complex biological indels.
- 🎯 **Banded DP Optimization**: Incorporates GPU-tailored banded DP pruning (`ABPOA_GPU_BAND`) to significantly reduce unnecessary cell computations while maintaining optimal alignment paths.
- 🚀 **High-Throughput Batch Processing**: Groups reads into concurrent batches and schedules intra-read wavefront parallelism across CUDA blocks to maximize hardware utilization.

---

## 📦 Download & Compilation

### Prerequisites
- GCC / G++ (>= 7.5)
- NVIDIA CUDA Toolkit (>= 11.0, with `nvcc`)
- GNU Make
- `zlib` development library

### Build Steps

```bash
# 1. Clone the repository
git clone https://github.com/BUGFRG/gnPOA.git
cd gnPOA

# 2. Compile with CUDA support (target Ampere / RTX 3090 as example)
make gpu=1 NVCC_ARCH=-arch=sm_86

# 3. Verify CUDA runtime linkage
ldd bin/abpoa | grep cudart
```

---

## 🚀 Usage

### 1. Produce Help Page

```bash
./bin/abpoa -h
```

---

### 2. Basic Alignment (CPU Mode)

Align a set of query sequences against a reference DAG (in `.gfa` format):

```bash
./bin/abpoa -i graph.gfa -r 4 -b -1 -o output_cpu.txt reads.fq
```

---

### 3. GPU-Accelerated Alignment

Add `-U` (or `--gpu`) to enable CUDA hardware acceleration:

```bash
./bin/abpoa -U -i graph.gfa -r 4 -b -1 -o output_gpu.txt reads.fq
```

---

### 4. High-Performance GPU Execution

To optimize throughput on large read sets, specify runtime environment variables along with the command:

```bash
ABPOA_GPU_BAND=8 \
ABPOA_GPU_BATCH=256 \
ABPOA_GPU_THREADS=128 \
./bin/abpoa -U -i graph.gfa -r 4 -b -1 -o output_gpu.txt reads.fq
```
