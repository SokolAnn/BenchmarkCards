# CLAW (Chinese Legal Knowledge Benchmark)

## 📊 Benchmark Details

**Name**: CLAW (Chinese Legal Knowledge Benchmark)

**Overview**: CLAW is a novel benchmark specifically engineered to meticulously evaluate Large Language Models (LLMs) on Chinese legal knowledge and its application in reasoning. It includes a corpus of all 306 Chinese national statutes segmented to the subparagraph level and a challenging set of 254 case-based reasoning instances derived from China Supreme Court curated materials.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- LawBench
- LexEval

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the depth of Chinese legal knowledge and the efficacy of case-based legal reasoning in general-purpose LLMs.

**Target Audience**:
- ML Researchers
- Legal practitioners
- Domain Experts

**Tasks**:
- Legal Knowledge Recall
- Case-Based Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: A comprehensive corpus of 306 Chinese national statutes and 254 case-based reasoning instances from the Supreme Court of China.

**Size**: 64,849 entries

**Format**: N/A

**Annotation**: Legal texts and reasoning cases are prepared based on authoritative sources and guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L
- Hierarchical accuracy

**Calculation**: Metrics are calculated as per defined tasks, focusing on hierarchical accuracy for ID Retrieval and similarity scores for Content Retrieval.

**Interpretation**: Higher scores indicate better performance in legal knowledge recall and reasoning capabilities.

**Baseline Results**: N/A

**Validation**: Empirical validation through comparisons with leading LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
