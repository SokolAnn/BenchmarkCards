# HaluEval 2.0

## 📊 Benchmark Details

**Name**: HaluEval 2.0

**Overview**: A benchmark designed for evaluating the factuality hallucination in large language models, consisting of 8,770 questions across multiple domains.

**Data Type**: Questions

**Domains**:
- Biomedicine
- Finance
- Science
- Education
- Open Domain

**Resources**:
- [GitHub Repository](https://github.com/RUCAIBox/HaluEval-2.0)

## 🎯 Purpose and Intended Users

**Goal**: To systematically study hallucinations in LLMs focusing on detection, source, and mitigation.

**Target Audience**:
- Researchers
- Developers in NLP
- AI practitioners

**Tasks**:
- Evaluating hallucination levels in LLMs
- Developing methodologies for hallucination detection
- Mitigating hallucination effects

**Limitations**: None

## 💾 Data

**Source**: Multiple domain datasets including BioASQ, NFCorpus, FiQA-2018, SciFact, LearningQ, and HotpotQA.

**Size**: 8,770 questions

**Format**: Text

**Annotation**: Questions selected based on difficulty and likelihood of hallucination.

## 🔬 Methodology

**Methods**:
- Framework for hallucination detection
- Statistical analysis of hallucination sources
- Empirical evaluation of mitigation strategies

**Metrics**:
- Micro hallucination rate (MiHR)
- Macro hallucination rate (MaHR)

**Calculation**: MiHR and MaHR are calculated based on the number of hallucinatory statements in responses.

**Interpretation**: Lower values indicate better performance in hallucination mitigation.

**Validation**: Validated via comparison with human labeling for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data was used in the construction of the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
