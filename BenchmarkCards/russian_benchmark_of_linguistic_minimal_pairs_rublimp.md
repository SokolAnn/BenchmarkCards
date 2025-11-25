# Russian Benchmark of Linguistic Minimal Pairs (RuBLiMP)

## 📊 Benchmark Details

**Name**: Russian Benchmark of Linguistic Minimal Pairs (RuBLiMP)

**Overview**: RuBLiMP is a benchmark consisting of 45 datasets, each including 1k minimal pairs that differ in grammaticality and isolate a linguistic phenomenon, covering various morphological, syntactic, and semantic aspects specific to Russian. It utilizes open text corpora and expert-written perturbation rules to generate these pairs.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- BLiMP
- CLiMP
- JBLiMP
- SLING
- CLAMS

**Resources**:
- [Resource](https://huggingface.co/datasets/RussianNLP/rublimp)
- [GitHub Repository](https://github.com/RussianNLP/RuBLiMP)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the grammatical knowledge of language models through minimal pairs that isolate specific linguistic phenomena in Russian.

**Target Audience**:
- ML Researchers
- Linguists
- Language Model Developers

**Tasks**:
- Grammaticality Judgments
- Linguistic Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Sentences extracted from open text corpora including Wikipedia and Russian literature, annotated and perturbed to create minimal pairs.

**Size**: 45,000 pairs

**Format**: JSONL

**Annotation**: Manual curation and validation by linguists

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy measured through comparison of model performance on generated minimal pairs.

**Interpretation**: A higher accuracy indicates better performance by models in identifying grammatical contrasts.

**Baseline Results**: Human performance averages around 95% accuracy on RuBLiMP.

**Validation**: Validated by 20 native speakers with linguistics backgrounds

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
