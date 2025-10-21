# CofCA (Step-wise Counterfactual Multi-hop QA benchmark)

## 📊 Benchmark Details

**Name**: CofCA (Step-wise Counterfactual Multi-hop QA benchmark)

**Overview**: A Step-wise Counterfactual benchmark (CofCA) consisting of factual data and counterfactual data that reveals LLMs’ real reasoning abilities on multi-step reasoning and reasoning chain evaluation by combining counterfactual passages with corresponding multi-hop QA pairs and sub-QA pairs.

**Data Type**: text (counterfactual and factual passages with multi-hop question-answer pairs and sub-question-answer pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- 2WikiMultihopQA
- MuSiQue
- DisentQA
- IfQA

**Resources**:
- [Resource](https://anonymous.4open.science/r/LLM_inherent_multi_step_eval-3818/)
- [Resource](https://huggingface.co/datasets/lucadiliello/english_wikipedia)
- [Resource](https://arxiv.org/abs/2402.11924)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' real multi-step reasoning ability and evidence integration by disentangling LLMs' internal memory from contextual reasoning via counterfactual multi-hop QA and explicit reasoning-chain evaluation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Multi-hop Question Answering
- Sub-question Answering
- Reasoning Chain Evaluation

**Limitations**: Dataset size remains to be improved. Exact Match (EM) has limitations for variations in answer expressions (e.g., aliases or abbreviations).

## 💾 Data

**Source**: 300 Wikipedia passages re-annotated into counterfactual passages (source passages sampled from Huggingface english_wikipedia). Control group: 900 factual MHQA examples (300 from HotpotQA, 300 from 2WikiMultihopQA, 300 from MuSiQue).

**Size**: 300 re-annotated Wikipedia passages; 900 multi-hop questions (one 2-hop, one 3-hop, one 4-hop per passage); 2,700 sub-questions; total of 3,600 unique QA pairs from re-annotated data. Additionally 900 factual MHQA control examples. Test set treated as 1,800 data.

**Format**: N/A

**Annotation**: Automatic LLM-based passage rewriting and QA generation with human-in-the-loop verification: (1) LLMs act as passage annotators to replace named entities, noun phrases, and synonyms and paraphrase via back-translation; (2) human experts manually evaluate grammatical integrity and verify that passages are new/counterfactual to LLMs; (3) LLMs generate multi-hop QA pairs and sub-questions; generated QA pairs are manually checked for grammar and answerability. For each passage, three complex questions were annotated (one 2-hop, one 3-hop, one 4-hop).

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (EM, F1)
- Partial match evaluation via GPT-4-turbo
- Reasoning chain evaluation (sub-question + final-answer chain analysis)
- Human-in-the-loop annotation and manual review

**Metrics**:
- Exact Match (EM)
- F1 Score
- Partial Match (PM) via GPT-4-turbo
- Joint F1RC (joint F1 of reasoning chain)
- Joint EMRC (joint EM of reasoning chain)
- Inter-annotator Agreement

**Calculation**: Joint performance: P(joint)=P(MHQA) * P(sub_qa1) * ... * P(sub_qaN); R(joint)=R(MHQA) * R(sub_qa1) * ... * R(sub_qaN). Joint F1RC and Joint EMRC are computed as the negative log2 of the combined joint precision/recall or EM terms as specified in Appendix B of the paper (formulas provided in the paper). Partial Match (PM) is measured using GPT-4-turbo to evaluate semantic partial matches between generated and gold answers.

**Interpretation**: Joint performance metrics are negative-log measures: larger Joint F1RC or Joint EMRC scores indicate worse performance on the full reasoning chain. EM and F1 measure sub-question and final-answer correctness; PM accounts for alias/abbreviation partial matches.

**Baseline Results**: Selected baseline results reported in the paper: On Wikipedia-based factual datasets (HotpotQA), GPT-4: EM 69.9, F1 82.3. On CofCA (2-hop), GPT-4: EM 53.1, F1 62.8. Across CofCA subsets (2-/3-/4-hop) and models, performance drops relative to Wikipedia-based factual data (tables in paper provide full breakdown for multiple proprietary and open-source LLMs).

**Validation**: Manual inspection: random 300 samples reviewed by two expert reviewers; overall inter-annotator agreement 94%. Per-hop human agreement reported as 96% (2-hop), 92% (3-hop), 95% (4-hop). GPT-4 used to assign correctness and informativeness binary scores for additional QC.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Accuracy
- Robustness

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Accuracy**: Data contamination, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
