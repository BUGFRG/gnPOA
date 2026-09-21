#ifndef ABPOA_GPU_H
#define ABPOA_GPU_H

#include "abpoa.h"

#ifdef __cplusplus
extern "C" {
#endif

int abpoa_gpu_align_sequence_to_graph(abpoa_t *ab, abpoa_para_t *abpt, uint8_t *query, int qlen, abpoa_res_t *res);
int abpoa_gpu_align_sequences_to_graph(abpoa_t *ab, abpoa_para_t *abpt, uint8_t **queries, int *qlens, int n_queries, abpoa_res_t *results);
const char *abpoa_gpu_last_error(void);
void abpoa_gpu_free_context(void *gpu_ctx);

#ifdef __cplusplus
}
#endif

#endif
