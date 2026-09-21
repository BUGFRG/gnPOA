fgpoa-gpu
fgpoa-gpu extends fgpoa with a CUDA backend for GPU-accelerated sequence-to-graph alignment. It performs the full DP scoring and traceback on GPU, supports batched processing of equal-length reads, and uses banded DP to reduce unnecessary computation — achieving ~14.8× speedup over the CPU path on 1M × 1000 bp reads (RTX 3090) with identical best_score results.

Download and Compile
sh

git clone https://github.com/zzzerd/fgpoa.git
cd fgpoa && make gpu=1 NVCC=/path/to/nvcc
By default the Makefile targets sm_86 (Ampere / RTX 3090). Override with NVCC_ARCH=-arch=sm_90 for Hopper, etc.

Verify the binary is linked to CUDA:

sh

ldd bin/abpoa | grep cudart
Usage
Help page

sh

bin/abpoa -h
CPU alignment (baseline):

sh

bin/abpoa -b -1 -i graph.gfa -o cpu.tsv reads.fa
GPU alignment:

sh

bin/abpoa -U -b -1 -i graph.gfa -o gpu.tsv reads.fa
Flag / Arg	Description
-U / --gpu	Enable CUDA sequence-to-graph DP
-b -1	Disable CPU adaptive band (for fair CPU/GPU comparison)
-i graph.gfa	Input graph (GFA format)
-o output.tsv	Output file
reads.fa	Input reads (FASTA/FASTQ)
GPU Environment Variables
sh

ABPOA_GPU_BATCH=256       # reads per batch
ABPOA_GPU_THREADS=128     # threads per CUDA block
ABPOA_GPU_BAND=8          # band width (0 = full DP)
ABPOA_GPU_SCORE_ONLY=1    # score only, skip traceback (CIGAR = *)
ABPOA_GPU_I16=1           # use 16-bit DP when safe
Recommended configuration (1000 bp reads / graph_81):

sh

ABPOA_GPU_BAND=8 ABPOA_GPU_BATCH=256 ABPOA_GPU_THREADS=128 \
  bin/abpoa -U -b -1 -i graph.gfa -o gpu.tsv reads.fa
Output Format
The output is tab-delimited. Each line consists of the read name, maximum score, matching path, and CIGAR string. The path is represented as a tuple of segments and base offsets.

Benchmark
Run the built-in benchmark script:

sh

scripts/benchmark_large_dataset.sh 1000     # quick 1k-read test
scripts/benchmark_large_dataset.sh full      # full 1M-read experiment
1M × 1000 bp Results (RTX 3090)
Wall Time	Speedup
CPU	21 min 19 s	—
GPU	1 min 26 s	14.8×
score_mismatches: 0 (GPU scores identical to CPU)
avg_gpu_utilization: 90.3 %
Peak GPU memory: 6285 MB
Current Limitations
Batch path requires equal-length reads within each batch.
One CUDA block per query; very long single reads cannot span multiple SMs.
local / extension modes fall back to CPU.
License
See fgpoa for license details.
