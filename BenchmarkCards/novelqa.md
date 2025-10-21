# NovelQA

## 📊 Benchmark Details

**Name**: NovelQA

**Overview**: NovelQA is a benchmark crafted to specifically evaluate LLMs’ performance on texts with averaged context windows exceeding 200,000 tokens, constructed from English novels to assess deep textual understanding in LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NarrativeQA
- LongBench
- HotpotQA

**Resources**:
- [Resource](https://novelqa.github.io/)
- [Resource](https://huggingface.co/datasets/NovelQA/NovelQA)
- [Resource](https://www.codabench.org/competitions/2727/)

## 🎯 Purpose and Intended Users

**Goal**: To assess the long-context comprehension abilities of LLMs using complex narratives from novels.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 65 free public-domain books from Project Gutenberg and 24 copyright-protected books purchased online.

**Size**: 2305 QA tuples

**Format**: JSON

**Annotation**: Annotations performed by expert annotators with detailed, human-crafted questions and corresponding answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model outputs compared to ground truth answers.

**Interpretation**: Higher accuracy indicates better model performance in understanding and responding to questions based on long textual contexts.

**Baseline Results**: Human baselines achieved around 90% accuracy in generative settings.

**Validation**: Evaluated with various long-context LLMs to assess their long-context understanding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: NovelQA does not contain any personally identifiable information.

**Data Licensing**: NovelQA is released under the Apache-2.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
