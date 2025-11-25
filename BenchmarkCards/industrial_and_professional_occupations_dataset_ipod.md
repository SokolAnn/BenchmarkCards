# Industrial and Professional Occupations Dataset (IPOD)

## 📊 Benchmark Details

**Name**: Industrial and Professional Occupations Dataset (IPOD)

**Overview**: This work presents the Industrial and Professional Occupations Dataset (IPOD), a publicly available corpus of occupation entries crawled from LinkedIn (192,295 job titles from 56,648 profiles). The paper demonstrates IPOD's usefulness by (i) proposing Title2vec, a contextual job-title vector representation using a bidirectional Language Model (biLM) approach, and (ii) addressing occupational Named Entity Recognition (NER) using Conditional Random Fields (CRF) and bidirectional LSTM-CRF models.

**Data Type**: text (job title entries)

**Domains**:
- Natural Language Processing
- Occupational Data Mining

**Languages**:
- English

**Similar Benchmarks**:
- CoNLL-2003
- Ontonotes
- CHEMDNER
- SQuAD
- APS (American Physical Society dataset)

**Resources**:
- [GitHub Repository](https://www.github.com/junhua/ipod)
- [Resource](https://arxiv.org/abs/1910.10495)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large, publicly available dataset of job title entries to support occupational data mining and analysis, and to enable upstream tasks such as job title embedding (Title2vec) and occupational Named Entity Recognition (NER).

**Target Audience**:
- Industry Practitioners
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Embedding (Job Title Embedding / Representation Learning)

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from LinkedIn profiles (Asia and the United States); 56,648 unique profiles.

**Size**: 192,295 occupation entries

**Format**: Formatted for NER tasks with BIOES tagging scheme

**Annotation**: Knowledge-based gazetteer created by three annotators (HR personnel, senior recruiter, seasoned business professional). Top 1,500 tokens were tagged; inter-rater reliability: 0.853 Percentage Agreement and 0.778 Cohen's Kappa. Labels use BIOES positional prefixes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match (EM)
- F1 Score
- Precision
- Recall

**Calculation**: F1 is computed as F1 = 2 * Precision * Recall / (Precision + Recall). Exact Match (EM) measures the percentage agreement between the ground truth and predicted labels with exact matches.

**Interpretation**: Higher EM and F1 indicate better NER performance. Human baseline reported as EM = 91.3% and F1 = 95.4%; models exceeding these are considered to outperform human baseline (paper reports CRF and LSTM-CRF outperform human and baselines in EM and F1).

**Baseline Results**: Reported overall results (Precision, Recall, EM, F1): LogReg: P 90.80 R 93.20 EM 85.10 F1 92.00; LSTM: P 99.71 R 99.90 EM 99.61 F1 99.80; CRF: P 99.90 R 99.81 EM 99.71 F1 99.85; LSTM-CRF: P 99.86 R 99.97 EM 99.83 F1 99.91; Human: P 91.60 R 99.60 EM 91.30 F1 95.40.

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The corpus comprises entries from United States (56.7%) and Asia (43.3%). Most titles fall within five words (91.7%). Median title length: overall 3 words; US median 3 words; Asia median 2 words — paper notes Asian titles tend to be shorter than US titles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
