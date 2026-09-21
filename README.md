# fgpoa (Folded Graph Partial Order Alignment)

<p align="center">
  <img src="https://img.shields.io/badge/Language-C-blue.svg" alt="Language">
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" alt="Build">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey.svg" alt="Platform">
</p>

---

**fgpoa** is designed to leverage a **folded genome graph structure** to deliver a fast, memory-efficient, and highly accurate method for **sequence-to-graph alignment**. It enhances both the sequence-to-graph scoring algorithm and the optimal alignment backtracking algorithm.

<p align="center">
  <img src="docs/folded_graph_structure.png" alt="Folded Graph Structure" width="650"/>
  <br>
  <em>Figure: Folded genome graph structure overview.</em>
</p>

---

## ✨ Key Features

- ⚡ **High Efficiency**: Fast alignment speed optimized for sequence-to-graph matching.
- 💾 **Low Memory Footprint**: Compact data structures tailored for folded DAG graphs.
- 🎯 **Accurate Backtracking**: Improved scoring and optimal path traceback algorithms.

---

## 📦 Download & Compile

### Prerequisites
- GCC / Clang (with C99 support)
- GNU Make
- `zlib` development library

### Build Steps

```bash
# 1. Clone the repository
git clone https://github.com/zzzerd/fgpoa.git

# 2. Enter directory and compile
cd fgpoa && make
```

---

## 🚀 Usage

### 1. View Help

```bash
./fgpoa -h
```

### 2. Align Reads to a Reference Graph

Align query sequences (`reads.fq`) against a reference DAG graph in **GFA** format (`graph.gfa`):

```bash
./fgpoa -i graph.gfa -r 4 -b -1 -o outputfile.txt reads.fq
```

#### Common Parameters

| Option | Argument | Description |
| :--- | :--- | :--- |
| `-i` | `FILE` | Reference DAG graph in `.gfa` format |
| `-r` | `INT` | Match / mismatch scoring parameters |
| `-b` | `INT` | Bandwidth / gap penalty parameter |
| `-o` | `FILE` | Output file path |
| `[reads]` | `FILE` | Query sequence file (`.fa`, `.fq`, `.fastq`, etc.) |

> [!NOTE]
> Currently, only **sequence-to-graph alignment** is supported. Sequence graph generation from scratch is not yet implemented.

---

## 📄 Output Format

The output is **tab-delimited (TSV)**, where each line represents an aligned query read with the following fields:

| Column | Field Name | Description |
| :---: | :--- | :--- |
| **1** | `Max Score` | Optimal alignment score |
| **2** | `Path Matching` | Path representation as tuples of segment IDs and base offsets: `(segment, offset)` |
| **3** | `CIGAR` | Standard alignment CIGAR string across the matched path |

### Example Output

```text
142    (seg1:0, seg2:15, seg5:0)    150M2D10M
```

---

## 📜 Citation & License

This project is open-source under the [MIT License](LICENSE).  
If you use **fgpoa** in your research, please cite:

```bibtex
@article{fgpoa,
  title={fgpoa: Fast and memory-efficient sequence-to-graph alignment with folded graph partial order alignment},
  author={zzzerd},
  year={2024}
}
```
