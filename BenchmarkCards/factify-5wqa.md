# FACTIFY-5WQA

## 📊 Benchmark Details

**Name**: FACTIFY-5WQA

**Overview**: A semi-automatically generated dataset called FACTIFY-5WQA consisting of 391,041 facts with corresponding 5W (who, what, when, where, why) question-answer pairs for aspect-based fact verification through question answering. A semantic role labeling system is used to locate 5Ws and generate QA pairs for claims using a masked language model; the paper also includes paraphrased claims, a baseline QA system to locate answers from evidence documents, and a proposed fact verification system that validates paraphrased claims.

**Data Type**: question-answering pairs (text: claims, paraphrased claims, 5W QA pairs, evidence documents)

**Domains**:
- Natural Language Processing
- Fact Checking
- Journalism

**Languages**:
- English

**Similar Benchmarks**:
- FEVER
- LIAR
- PolitiFact
- FaVIQ
- HoVer
- X-Fact
- CREAK
- FEVEROUS
- Factify 1.0
- Factify 2.0
- VITC

**Resources**:
- [GitHub Repository](https://github.com/ankuranii/acl-5W-QA)

## 🎯 Purpose and Intended Users

**Goal**: Provide a 5W aspect-based question-answer dataset and framework to enable aspect-based explainable fact verification and to support development and evaluation of QA and fact verification systems.

**Target Audience**:
- Human fact-checkers
- ML Researchers
- Model Developers
- Journalists

**Tasks**:
- Question Answering
- Fact Verification
- Question Generation
- Text Paraphrasing
- Semantic Role Labeling
- Evidence Retrieval

**Limitations**: Paraphrasing: automatic paraphrasing may not generate complex meaning-preserving variations and can produce problematic paraphrases. 5W SRL: mapping can fail in elliptic situations like anaphora and cataphora. 5W QA pair generation: automatic generation may miss more complex multi-W or how-type questions. QA system: generated performance indicates the proposed QA model needs substantial improvement. Relevant document retrieval remains a major bottleneck.

## 💾 Data

**Source**: Amalgamation of existing fact verification datasets: selected and filtered claims from FEVER, HoVer, VITC, FaVIQ, Factify 1.0, and Factify 2.0 after filtering 121 publicly available fact verification datasets.

**Size**: 391,041 claims; 1,741,131 paraphrased claims; 903,305 5W QA pairs; 357,116 evidence documents

**Format**: N/A

**Annotation**: Semi-automatically generated via semantic role labeling (SRL) mapping to 5W and masked language model-based QA/paraphrase generation, with human evaluation/annotation on random samples (3,000 data points: 500 random data points each from FEVER, FaVIQ, HoVer, VITC, Factify 1.0, Factify 2.0) for mapping and QA generation.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (QG and QA models: ProphetNet, BART, T5-3B, T5-Large, BERT-Large)
- Automated metrics (BLEU Score, ROUGE-L, Recall, F1 Score, inverse-BLEU diversity)
- Human evaluation (annotation of random samples for mapping accuracy and QA quality)

**Metrics**:
- BLEU Score
- ROUGE-L
- Recall
- F1 Score
- Diversity (inverse BLEU)
- Coverage (%)
- Correctness (%)
- Mapping accuracy (%)
- Human agreement (%)

**Calculation**: Coverage: number of paraphrases (up to 5) with minimum edit distance (MED) > 2 words. Correctness: pairwise entailment checked using RoBERTa Large trained on SNLI. Diversity: computed as inverse BLEU score between paraphrases. QA evaluation: BLEU/ROUGE-L/Recall/F1 between generated and gold answers. Human evaluation: percentage agreement on sampled 3,000 data points for question well-formedness, question correctness, and answer correctness; mapping accuracy measured on 3,000 annotated data points (500 per source).

**Interpretation**: Higher BLEU/ROUGE-L/Recall/F1 indicate better QA generation/validation performance; higher diversity (inverse BLEU) indicates more linguistic variation in paraphrases; human agreement percentages indicate quality of SRL mapping and QA generation. The best QAG-Validation model combination identified in experiments is ProphetNet (QAG) + T5-3B (QA validation).

**Baseline Results**: Paraphrasing models: Pegasus - Coverage 32.46, Correctness 94.38%, Diversity 3.76; T5 - Coverage 30.26, Correctness 83.84%, Diversity 3.17; GPT-3 (text-davinci-003) - Coverage 35.51, Correctness 88.16%, Diversity 7.72. Best QAG-Validation combination identified: ProphetNet (QAG) + T5-3B (QA). (Results and detailed scores reported in Table 3 and Table 5 of the paper.)

**Validation**: Human evaluation on random sample of 3,000 data points (500 from each source) for SRL mapping and QA generation; QA validation using models T5-3B, T5-Large, and BERT-Large with automated metrics (BLEU, ROUGE-L, Recall, F1).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
