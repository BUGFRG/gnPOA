import sys
import re

with open("src/abpoa_gpu.cu", "r") as f:
    code = f.read()

# Replace the original function name
code = code.replace("int abpoa_gpu_align_sequences_to_graph_orig(", "int abpoa_gpu_align_sequences_to_graph(")

# Add timing prints
patch = """
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    float ms;

    cudaEventRecord(start);
"""

code = code.replace("if (ensure_dp_buffers(ctx, batch_cells, dp_bytes, max_qlen) != 0)", patch + "if (ensure_dp_buffers(ctx, batch_cells, dp_bytes, max_qlen) != 0)")

patch_dp = """
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&ms, start, stop);
    fprintf(stderr, "Alloc & copy to device: %f ms\\n", ms);
    cudaEventRecord(start);

    abpoa_gpu_dp_batch_kernel<<<n_queries, threads>>>(
"""
code = code.replace("abpoa_gpu_dp_batch_kernel<<<n_queries, threads>>>(", patch_dp)

patch_tb = """
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&ms, start, stop);
    fprintf(stderr, "DP kernel: %f ms\\n", ms);
    cudaEventRecord(start);

    abpoa_gpu_traceback_batch_kernel<<<n_queries, 1>>>(
"""
code = code.replace("abpoa_gpu_traceback_batch_kernel<<<n_queries, 1>>>(", patch_tb)

patch_end = """
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    cudaEventElapsedTime(&ms, start, stop);
    fprintf(stderr, "Traceback & copy back: %f ms\\n", ms);

    return 0;
"""
code = code.replace("return 0;", patch_end)

with open("src/abpoa_gpu.cu", "w") as f:
    f.write(code)
