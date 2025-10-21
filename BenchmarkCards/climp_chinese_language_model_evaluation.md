# CLiMP (Chinese Language Model Evaluation)

## 📊 Benchmark Details

**Name**: CLiMP (Chinese Language Model Evaluation)

**Overview**: CLiMP consists of 1,000 minimal pairs for 16 syntactic contrasts in Mandarin, covering 9 major Mandarin linguistic phenomena, providing a framework for evaluating the knowledge of Chinese language models.

**Data Type**: minimal pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- BLiMP (Benchmark of Linguistic Minimal Pairs)

**Resources**:
- [Resource](https://nalacub.github.io/resources)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate which syntactic phenomena Chinese language models can learn and improve upon.

**Target Audience**:
- ML Researchers
- Model Developers
- Linguists

**Tasks**:
- Linguistic Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Semi-automatically generated from grammar templates.

**Size**: 16,000 minimal pairs

**Format**: N/A

**Annotation**: Human agreement with labels is 95.8%.

## 🔬 Methodology

**Methods**:
- Accuracy evaluation

**Metrics**:
- Accuracy

**Calculation**: A minimal pair is classified correctly if a language model assigns a higher probability to the grammatical sentence than the ungrammatical one.

**Interpretation**: Higher accuracy indicates better understanding of syntactic phenomena.

**Baseline Results**: Chinese BERT achieved 81.8% accuracy on average across all phenomena.

**Validation**: Human agreement was found to be over 95%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
