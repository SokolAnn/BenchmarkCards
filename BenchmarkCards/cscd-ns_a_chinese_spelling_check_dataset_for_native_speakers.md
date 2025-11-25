# CSCD-NS (a Chinese Spelling Check Dataset for Native Speakers)

## 📊 Benchmark Details

**Name**: CSCD-NS (a Chinese Spelling Check Dataset for Native Speakers)

**Overview**: In this paper, we present CSCD-NS, the first Chinese spelling check (CSC) dataset designed for native speakers, containing 40,000 samples from a Chinese social platform. Compared with existing CSC datasets aimed at Chinese learners, CSCD-NS is ten times larger in scale and exhibits a distinct error distribution, with a significantly higher proportion of word-level errors. To further enhance the data resource, we propose a novel method that simulates the input process through an input method, generating large-scale and high-quality pseudo data that closely resembles the actual error distribution and outperforms existing methods. Moreover, we investigate the performance of various models in this scenario, including large language models (LLMs), such as ChatGPT.

**Data Type**: text (sentence-level spelling correction pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese (Simplified)

**Similar Benchmarks**:
- SIGHAN13
- SIGHAN14
- SIGHAN15

**Resources**:
- [GitHub Repository](https://github.com/nghuyong/cscd-ns)
- [Resource](https://arxiv.org/abs/2211.08788)
- [Resource](https://www.google.com/inputtools/)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the first Chinese spelling check dataset for native speakers (CSCD-NS), analyze the error distribution for native speakers, propose an IME-based pseudo-data construction method, and evaluate various models (including LLMs) on this scenario.

**Target Audience**:
- ML Researchers

**Tasks**:
- Error Detection
- Spelling Correction

**Limitations**: The data source for the CSCD-NS dataset is derived from a Chinese social networking platform and may not fully represent the error distribution of native speakers in other scenarios (e.g., formal document writing). The IME-based pseudo-data construction method is relatively basic and may not accurately simulate realistic input scenarios such as abbreviated pinyin or T9-style mobile input.

## 💾 Data

**Source**: LCSTS (authentic Weibo posts)

**Size**: 40,000 examples (30,000 training samples, 5,000 development samples, 5,000 test samples); pseudo dataset LCSTS-IME-2M: ~2,000,000 examples

**Format**: N/A

**Annotation**: Manual annotation by native speakers; each sentence annotated at least twice by different annotators; disagreements resolved by a senior annotator. Sentences with inherent ambiguity, multiple reasonable corrections, or complex grammatical errors were discarded.

## 🔬 Methodology

**Methods**:
- Automated metrics (precision, recall, F1) at sentence and character level
- Model evaluation via full-parameter fine-tuning
- Low-rank adaptation (LoRA) fine-tuning
- In-context learning (ICL) evaluation for ChatGPT/GPT4
- Pretraining on pseudo data followed by fine-tuning on labeled data

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Sentence-level metrics use the calculation method in FASPell (Hong et al., 2019). Character-level metrics calculate all characters (not only those correctly detected). Detection and correction metrics are computed at both sentence and character level.

**Interpretation**: Higher precision/recall/F1 indicate better detection and correction. The paper notes that BERT-like token-level classification models outperform generative models in this task. The authors report that the best F1 score of baseline models is still below 80, indicating the task remains challenging, especially due to a high proportion of word-level errors.

**Baseline Results**: Selected results from Table 4 (character-level correction F1): BERT: 65.75%; BERT + LCSTS-IME-2M: 75.63%; Baichuan2-13B: 59.60%; Baichuan2-13B + LCSTS-IME-2M: 65.48%; ChatGPT: 52.63%; GPT4: 54.57%.

**Validation**: For each experiment the best checkpoint is selected based on the development set and evaluated on the test set. Experiments are run three times and the reported results are averages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Intellectual Property

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Intellectual Property**: Data usage rights restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The CSCD-NS and the constructed pseudo-data LCSTS-IME-2M are based on LCSTS. The authors applied for and obtained the right to use LCSTS and performed the academic research under the copyright.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
