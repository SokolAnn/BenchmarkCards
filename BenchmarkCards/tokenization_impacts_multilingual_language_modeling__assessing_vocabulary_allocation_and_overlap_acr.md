# Tokenization Impacts Multilingual Language Modeling: Assessing Vocabulary Allocation and Overlap Across Languages

## 📊 Benchmark Details

**Name**: Tokenization Impacts Multilingual Language Modeling: Assessing Vocabulary Allocation and Overlap Across Languages

**Overview**: We introduce new criteria to evaluate the quality of lexical representation and vocabulary overlap observed in sub-word tokenizers, propose measures of vocabulary allocation and vocabulary overlap, and study how these tokenizer properties affect multilingual language model representation and downstream tasks (POS, dependency labeling, NER, NLI, cross-lingual sentence retrieval).

**Data Type**: text (tokenized multilingual corpora and downstream task datasets)

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Chinese
- Greek
- Turkish
- Spanish
- English
- Hebrew
- Georgian
- Urdu
- Hindi
- Marathi
- Thai
- Tamil
- Telugu
- Bulgarian
- Russian
- Swahili
- Vietnamese
- French
- German

**Similar Benchmarks**:
- XTREME
- XNLI
- Tatoeba
- Wikiann
- Universal Dependencies

**Resources**:
- [GitHub Repository](https://github.com/tomlimi/entangled_in_scripts)
- [Resource](https://arxiv.org/abs/2305.17179)
- [Resource](https://data.statmt.org/cc-100/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a framework and metrics to evaluate multilingual subword tokenizers (vocabulary allocation and vocabulary overlap) and to assess how tokenizer properties impact multilingual language model pre-training and downstream task performance.

**Target Audience**:
- Model Developers
- ML Researchers

**Tasks**:
- Masked Language Modeling
- Part of Speech Tagging
- Named Entity Recognition
- Dependency Labeling
- Natural Language Inference
- Cross-lingual Sentence Retrieval

**Limitations**: Models were scaled down for computational efficiency (smaller than XLM-Roberta); evaluation used linear probes on frozen representations rather than full fine-tuning. (Section 'Limitations')

## 💾 Data

**Source**: 10% of CC-100 corpus (subsampled per language following Conneau and Lample methodology) for tokenizer and model pretraining; downstream datasets: XTREME collection including XNLI, Tatoeba (sentence retrieval), Wikiann (NER), Universal Dependencies (POS and dependency labeling).

**Size**: Pretraining data: 10% of CC-100 (per-language subsampling with cmin = 10M characters and balancing parameter α = 0.25); vocabulary size N = 120,000; experiments run on sets of 6 languages and 20 languages. (Exact corpus sizes per language vary; cmin specified as 10M characters.)

**Format**: Raw text corpora (CC-100) and standard dataset formats for XTREME tasks (existing annotated datasets such as Universal Dependencies, Wikiann, XNLI, Tatoeba).

**Annotation**: Uses existing annotations from downstream datasets: Universal Dependencies (POS and dependency relations), Wikiann (NER in IOB2), XNLI (NLI labels), Tatoeba (aligned sentence pairs).

## 🔬 Methodology

**Methods**:
- Automated tokenizer metrics (vocabulary allocation measures: Average Rank (AR), Characters per Token (CPT); vocabulary overlap: Jensen-Shannon Divergence (JSD))
- Model-based evaluation: pretraining small transformer models (scaled XLM-R settings) and measuring Masked Language Modeling
- Probing: linear probes trained on frozen pre-trained model representations for downstream tasks (word-level and sentence-level probes)
- Correlation analysis (Spearman) across tokenizers and tasks

**Metrics**:
- Average Rank (AR)
- Characters per Token (CPT)
- Jensen-Shannon Divergence (JSD)
- Mean Reciprocal Rank (MRR) for masked language modeling
- F1 Score (macro-average) for POS, NER, and dependency labeling
- Accuracy for Natural Language Inference (XNLI) and Sentence Retrieval

**Calculation**: AR and CPT are computed on empirical token distributions per language (Equations 3-5). JSD is computed between language token probability distributions (Equations 6-7). MRR is computed as mean reciprocal rank over masked-token prediction ranks (Equation 8). Downstream task metrics follow standard dataset evaluations (macro F1 for token-level tasks, accuracy for XNLI and retrieval).

**Interpretation**: Higher vocabulary allocation (higher AR, longer CPT) correlates with improved word-level downstream performance (POS, dependency labeling, NER) and better cross-lingual transfer for word-level tasks; higher vocabulary overlap (lower JSD) benefits NER and sentence-level tasks (NLI, sentence retrieval). Higher CPT negatively correlates with MLM MRR. These interpretations are supported by Spearman correlations and averaged probe results across tokenizers and language sets.

**Baseline Results**: Averaged in-language results for 6-language experiments (Table 2a): Unigram — AR 2042, CPT 3.17, MRR 42.0, NER F1 62.8, POS F1 57.1, Dependency F1 48.1, NLI Acc 53.4. BPE — AR 2193, CPT 4.47, MRR 35.6, NER 70.4, POS 68.9, Dep 58.7, NLI 53.3. NoOverlap — AR 1829, CPT 3.16, MRR 42.7, NER 69.4, POS 69.2, Dep 58.8, NLI 53.0. TokMix — AR 2198, CPT 3.34, MRR 38.7, NER 70.2, POS 67.3, Dep 57.3, NLI 53.3.

**Validation**: Experiments validated on two settings: a 6-language diverse set and a broader 20-language set. Probing results averaged across random seeds (5 seeds for 6-language experiments, 3 seeds for 20-language experiments). Statistical support via Spearman correlation analysis for metrics and task scores.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
