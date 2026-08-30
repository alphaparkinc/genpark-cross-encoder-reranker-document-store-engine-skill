from client import CrossEncoderRerankerDocumentStoreEngineClient

def main():
    client = CrossEncoderRerankerDocumentStoreEngineClient()
    res = client.rerank_candidate_documents('Explain Byzantine Fault Tolerance in Tendermint Core', 40, 3)
    print('Cross-Encoder Reranker: ' + res['reranking_job_id'])
    print('Filtered: ' + str(res['initial_retrieved_count']) + ' -> Top ' + str(res['top_k_reranked_count']) + ' (MRR: ' + str(res['mean_reciprocal_rank_mrr']) + ')')
    print('Top Passage: ' + res['top_scoring_passage_id'])

if __name__ == '__main__':
    main()
