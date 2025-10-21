# KorQuAD1.0 : Korean QA Dataset for Machine Reading Comprehension

## 📊 Benchmark Details

**Name**: KorQuAD1.0 : Korean QA Dataset for Machine Reading Comprehension

**Overview**: We present Korean Question Answering Dataset( KorQuAD ), a large-scale Korean dataset for extractive machine reading comprehension task. It consists of 70,000+ human generated question-answer pairs on Korean Wikipedia articles. We release KorQuAD1.0 and launch a challenge at https:// KorQuAD .github.io to encourage the development of multilingual natural language processing research.

**Data Type**: question-answering pairs (extractive)

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- SQuAD (Stanford Question Answering Dataset)
- SQuAD2.0
- Hotpot QA
- MS Marco (Microsoft Machine Reading Comprehension Dataset)
- K-QuAD

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To introduce KorQuAD1.0, a large-scale standard question-answering dataset for Korean extractive machine reading comprehension and to contribute to researchers in multilingual natural language processing by providing training data and an official evaluation challenge.

**Target Audience**:
- Researchers in multilingual natural language processing

**Tasks**:
- Question Answering
- Machine Reading Comprehension (Extractive)

**Limitations**: 2.9% of the questions are due to errors of the worker (errors in questioning). F1 is computed at character-level because morpheme analysis is imperfect for the Korean language.

## 💾 Data

**Source**: Korean Wikipedia articles (1,647 articles collected; passages extracted from these articles; selected from 'Alchan-geul' and 'Joeun-geul' lists plus random sampling).

**Size**: 70,079 question-answer pairs; 1,647 articles collected. Train: 1,420 articles, 9,681 paragraphs, 60,407 questions; Dev: 140 articles, 964 paragraphs, 5,774 questions; Test: 77 articles, 623 paragraphs, 3,898 questions.

**Format**: N/A

**Annotation**: Crowdsourced by crowdworkers: one passage allocated to 3 workers, each worker created up to 3 questions per passage; workers typed questions in natural language and were asked to select a minimal answer span in the morpheme unit. Additional workers generated secondary (shortest-span) answers on the test dataset.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Baseline model evaluation

**Metrics**:
- Exact Match (EM)
- Character-level F1

**Calculation**: EM: This metric measures the percentage of predictions that exactly match the ground truth answer. F1: This metric measures the overlap between the prediction and the ground truth answer. We adopt character-level F1 that compute the percentage of overlapping characters.

**Interpretation**: EM measures the percentage of exact matches; character-level F1 measures overlap of characters between prediction and ground truth; higher values indicate better performance. The paper does not provide explicit numeric thresholds for good vs. poor performance.

**Baseline Results**: Validation set: S³-Net EM 71.68%, F1 82.87%; BERT EM 70.89%, F1 90.24%. Test set: S³-Net EM 71.52%, F1 82.99%; BERT EM 71.68%, F1 89.76%. Human (test set) F1 91.20%. Total collected question-answer pairs: 70,079.

**Validation**: Data split into Train/Dev/Test (Train: 1,420 articles; Dev: 140; Test: 77). Additional workers generated secondary answers on the test dataset to compare human performance. A sample of 280 development questions (two per 140 paragraphs) was used for qualitative analysis of reasoning types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
