# BORDER LINES

## 📊 Benchmark Details

**Name**: BORDER LINES

**Overview**: A multilingual dataset and evaluation suite for measuring geopolitical bias in large language models via territorial disputes. BORDER LINES covers disputed territories with multiple-choice questions translated into the claimant countries' languages (49 languages) and metrics to quantify factual recall, geopolitical bias, and consistency across languages.

**Data Type**: text (multiple-choice question-answer pairs, multilingual) and tabular (territory metadata)

**Domains**:
- Natural Language Processing
- Political Science

**Languages**:
- Chinese
- Tagalog
- Vietnamese
- Spanish
- Arabic
- Ukrainian
- Russian
- Hindi
- Urdu
- Traditional Chinese
- Simplified Chinese

**Similar Benchmarks**:
- GeoM-LAMA
- MEGA: Multilingual evaluation of generative ai

**Resources**:
- [GitHub Repository](https://github.com/manestay/borderlines)
- [Resource](https://arxiv.org/abs/2305.14610)
- [Resource](https://translate.google.com)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate whether multilingual LLMs recall geopolitical knowledge differently when queried in different languages (geopolitical bias), by introducing a multilingual dataset of territorial dispute multiple-choice questions and an evaluation suite measuring factual recall, geopolitical bias, and consistency.

**Target Audience**:
- ML Researchers
- NLP Researchers
- Model Developers

**Tasks**:
- Question Answering
- Bias Evaluation
- Multilingual Consistency Evaluation

**Limitations**: Translations created via template-wise machine translation using Google Translate, which performs better on high-resource languages and may produce inconsistencies or grammatical errors for low-resource or highly-inflected languages; rank-classification was not implemented for GPT-4 due to inaccessible log-probabilities; the dataset is based on a snapshot of the English Wikipedia page (2023-05-15) and territorial statuses can change over time.

## 💾 Data

**Source**: English Wikipedia 'List of territorial disputes' (May 15, 2023 version); demographic information (majority language and religion) sourced from Wikipedia and other cited sources as described in Appendix A.

**Size**: 251 disputed territories; 726 multiple-choice questions; 49 claimant languages represented

**Format**: N/A

**Annotation**: Questions generated via template-wise machine translation (Google Translate) with preserved placeholders for entities; demographic fields (majority language and religion) extracted from Wikipedia. (No large-scale human translation/annotation of all queries reported.)

## 🔬 Methodology

**Methods**:
- Automated evaluation using rank-classification (log-probability ranking) for models with accessible log-probabilities
- Parsing of generated short-answer responses for GPT-4 (manual inspection for a small number of responses)
- Template-wise machine translation to create multilingual query sets
- Quantitative metric computation over entire dataset

**Metrics**:
- Concurrence Score (CS)
- KB CS (Knowledge Base Concurrence Score)
- Con CS (Controller-language CS)
- Non CS (Non-controller-language CS)
- ∆CS (Delta CS)
- Consistency CS (Cst CS)

**Calculation**: CS(ci, cj) = 100 * (1 if ci = cj else 0). KB CS compares English response to KB controller. Con CS compares controller-language response to KB. Non CS averages comparisons of non-controller-language responses to KB. ∆CS = (Con CS - Non CS) / Non CS (normalization by Non CS). Consistency CS is the average pairwise CS across a model's multilingual responses for a territory.

**Interpretation**: KB CS measures factual recall (higher is better). ∆CS quantifies geopolitical bias (∆CS = 0 indicates no language-dependent bias; larger positive values indicate greater bias toward controller-language responses). Consistency CS measures how similarly a model answers the same query across languages (higher indicates more consistent cross-lingual recall).

**Baseline Results**: Random baseline: KB CS = 43.5. Examples from reported results: BLOOM 560M — KB CS 61.5, Con CS 67.7, Non CS 31.2, ∆CS (relative) 115.0, Consistency CS (all) 50.7. GPT-4 (vanilla) — KB CS 79.5, Con CS 76.9, Non CS 63.2, ∆CS 21.6, Consistency CS (all) 70.8. (See paper Tables 5, 6, 8 for full results across models and prompt strategies.)

**Validation**: Validation includes applying the evaluation suite to temporal variants of the dataset (BORDER LINES 2021-09 vs BORDER LINES 2023-05-15) and manual inspection/qualitative case studies; authors report overall trends remained similar across temporal versions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy
- **Multi-category**: Prompt priming
- **Societal Impact**: Impact on affected communities, Impact on cultural diversity

**Demographic Analysis**: Dataset includes majority language and majority religion for each country; authors use these demographics in a 'demographic reasoning' prompt strategy and analyze its effects on model responses.

**Potential Harm**: ['Amplifying divisions in viewpoints across cultures', 'Polarization due to inconsistent factual information across languages', 'Misinformation arising from inconsistent cross-lingual factual recall']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
