# CroCoSum: A Benchmark Dataset for Cross-Lingual Code-Switched Summarization

## 📊 Benchmark Details

**Name**: CroCoSum: A Benchmark Dataset for Cross-Lingual Code-Switched Summarization

**Overview**: To study the phenomenon of code-switching in cross-lingual summarization, we introduce CroCoSum, a dataset of cross-lingual code-switched summarization of technology news. It consists of over 24,000 English source articles and 18,000 human-written Chinese news summaries, with more than 92% of the summaries containing code-switched phrases.

**Data Type**: text (source article — target summary pairs; English source articles and Chinese-English code-switched summaries)

**Domains**:
- Natural Language Processing
- News
- Technology

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- En2ZhSum
- XSAMSum
- XMediaSum40k
- WikiLingua
- CrossSum
- GupShup

**Resources**:
- [GitHub Repository](https://github.com/RosenZhang/CroCoSum)
- [Resource](https://archive.org/)
- [GitHub Repository](https://github.com/codelucas/newspaper)
- [GitHub Repository](https://github.com/Mimino666/langdetect)
- [GitHub Repository](https://github.com/uliontse/translators)
- [Resource](https://arxiv.org/abs/2303.04092v2)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset and benchmark to examine code-switching in cross-lingual summarization and to evaluate baseline approaches (pipeline, end-to-end, zero-shot) on human-written Chinese-English code-switched summaries of English technology news.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Natural Language Processing Researchers

**Tasks**:
- Cross-Lingual Summarization
- Abstractive Summarization
- Code-switched Text Generation

**Limitations**: Baseline experiments are limited by local compute and model sizes. Scope is restricted to topics covered by the data source (technology news). Code-switching in CroCoSum is predominantly in the form of named entities and product/scientific terms; cultural contexts and broader code-switching practices across different linguistic and cultural backgrounds may not be fully encapsulated.

## 💾 Data

**Source**: Target summaries collected from solidot.org (Chinese online platform where users compose Chinese summary posts referencing external English news links). Original English source articles were obtained from the Internet Archive by following embedded links in posts and retained only if detected as English.

**Size**: 18,557 human-written Chinese-English code-switched summaries; 24,171 English source articles

**Format**: N/A

**Annotation**: Summaries are human-written and reviewed by solidot.org editors prior to publication. For quality validation, 3 bilingual annotators rated a random sample of 20 source-target pairs using Fluency, Coherence, Informativeness and Relevance on a 5-point Likert scale (scores: F: 4.62, C: 4.95, I: 3.97, R: 4.18). Data is partitioned into training (70%), validation (15%), and test (15%) splits.

## 🔬 Methodology

**Methods**:
- Pipeline (translate-then-summarize; summarize-then-translate) using Google Translate API as translation module
- End-to-end finetuning of multilingual seq2seq models (mT5, mBART, mBART-50)
- Zero-shot prompting with GPT-3 and GPT-3.5
- Human qualitative analysis of generated summaries (error categorization and human ratings)

**Metrics**:
- ROUGE-1 (F1)
- ROUGE-2 (F1)
- ROUGE-L (F1)
- BERTScore
- Code-Switched Percentage (Sents. cs%)
- Code-Mixing Index (CMI)
- Intra-Sentence Switch Points (SP)
- Average sentence and word counts

**Calculation**: ROUGE F1 scores and BERTScore are computed between predicted and ground-truth summaries. Code-Mixing Index (CMI) computed per Gambäck and Das (2016) as fraction of language-dependent tokens not belonging to the matrix language (CMI(x) = (N(x) - max_Li t_Li(x)) / N(x), or 0 if N(x)=0). SP counts word boundaries within a sentence where adjacent words are in different languages. Code-switched percentage is the proportion of sentences containing code-switching spans.

**Interpretation**: Higher ROUGE and BERTScore indicate greater lexical and semantic similarity to human references. Smaller differences in code-switching metrics (code-switched percentage, CMI, SP) between predictions and gold summaries indicate model outputs more closely resemble human code-switching behavior. N-gram-based automatic metrics may fail to capture semantically correct code-switching choices.

**Baseline Results**: Best reported baseline: end-to-end finetuned mBART-50 (ROUGE-1: 38.73, ROUGE-2: 20.34, ROUGE-L: 34.35, BERTScore: 58.81). Zero-shot GPT-3 yielded ROUGE-1 26.50 / ROUGE-2 12.33 / ROUGE-L 24.00; GPT-3.5 showed improved scores (ROUGE-1 34.98 / ROUGE-2 17.75 / ROUGE-L 31.17). Pretraining on existing CLS resources (WikiLingua, CrossSum) before finetuning did not improve performance on CroCoSum.

**Validation**: Dataset split into training (70%), validation (15%), and test (15%). Quality validation: 3 bilingual annotators rated 20 randomly sampled pairs on Fluency, Coherence, Informativeness, and Relevance (5-point Likert). Best model checkpoints selected based on validation performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Robustness**: Hallucination
- **Governance**: Lack of testing diversity
- **Societal Impact**: Impact on cultural diversity, Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
