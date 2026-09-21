fgpoa
========================================================================

fgpoa is a sequence-to-graph alignment tool. It restores a normal reference DAG from GFA `S`/`L` records or FASTA, aligns each query sequence to the fixed graph, and reports the best alignment score and compact CIGAR.

## Download and compile



```sh
git clone https://github.com/zzzerd/fgpoa.git
cd fgpoa && make
```



## Usage

* Produce help page
```sh
abpoa -h
```

* Align a set of query sequences against a reference DAG (in .gfa format):
```sh
abpoa -i graph.gfa -b -1 -o outputfile.txt reads.fq
```


**Note:**  Currently only sequence-to-graph alignment is supported and sequence graph cannot be generated.

**Output file format:** The output is tab-delimited with each line consisting of query name, `best_score`, and compact CIGAR.

```text
query_name<TAB>best_score:<score><TAB>cigar:<cigar>
```

## <a name=“publication”></a>Publication

- **Yanfei Deng, Jinjun Kang, Zhuang Liu, Xiao Zhu, Wei Quan**. "[Fast sequence to graph alignment based on graph folding](10.1109/BIBM62325.2024.10822090)". *2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM). IEEE, 2024: 5194-5201*.
