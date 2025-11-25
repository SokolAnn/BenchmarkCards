# paraLFQA (Paraphrased Long-Form Question and Answer) and paraWP (Paraphrased Writing Prompts)

## 📊 Benchmark Details

**Name**: paraLFQA (Paraphrased Long-Form Question and Answer) and paraWP (Paraphrased Writing Prompts)

**Overview**: These datasets are created for the purpose of detecting document-level paraphrased Machine Generated Content (MGC). The paraLFQA dataset consists of paraphrased question and answer pairs, while the paraWP dataset includes paraphrased prompts.

**Data Type**: question-answering pairs, text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Plagbench
- M4

**Resources**:
- [Resource](https://drive.google.com/file/d/1fvsWwHKplf0-n6PnwbxIRmR6jgu62nRi/view?usp=sharing)

## 🎯 Purpose and Intended Users

**Goal**: To provide datasets for further research and evaluation in detecting paraphrased machine-generated content, particularly at the document level.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: A. We only report three sentence patterns, or writing styles, that affect GPTZero’s detection. It could be a future direction to find ways to embed these writing styles into automatic detection methods.

## 💾 Data

**Source**: The datasets consist of synthesized text pairs from original human-written content and their corresponding machine-generated revisions using specific models such as GPT and DIPPER.

**Size**: Around 2,000 pairs for paraLFQA; 166,247 documents for paraWP.

**Format**: JSON

**Annotation**: Automatically generated using discourse analysis tools.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- BLEU Score

**Calculation**: Metrics are derived based on comparisons between machine-generated and human-written versions, with BLEU score measuring n-gram overlap.

**Interpretation**: Higher scores indicate better performance in distinguishing between MGC and HPC.

**Validation**: Best results achieved through models integrating human-writing styles and discourse features.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under a Creative Commons Attribution 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
