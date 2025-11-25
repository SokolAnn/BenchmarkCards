# Machine Translation Commonsense Reasoning Test Suite

## 📊 Benchmark Details

**Name**: Machine Translation Commonsense Reasoning Test Suite

**Overview**: This paper presents a test suite to evaluate the commonsense reasoning capability of neural machine translation, consisting of three test sets covering lexical and contextless/contextual syntactic ambiguity that requires commonsense knowledge to resolve. The test suite aims to promote future research on commonsense reasoning in machine translation models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- Social IQA
- Event2mind
- Atomic
- WinoGram Schema Challenge
- SWAG
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/tjunlp-lab/CommonMT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the commonsense reasoning capability of state-of-the-art neural machine translation models and provide a benchmark testbed for tracking progress in this direction.

**Target Audience**:
- ML Researchers
- Translation Practitioners
- Model Developers

**Tasks**:
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Manually constructed data consisting of source sentences with ambiguity requiring commonsense reasoning, covering three types of ambiguities: lexical ambiguity, contextless syntactic ambiguity, and contextual syntactic ambiguity.

**Size**: 1,200 triples

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Commonsense Reasoning Accuracy

**Calculation**: The commonsense reasoning accuracy is calculated based on how well the NMT models can distinguish between correct and incorrect translations of ambiguous sentences by scoring each translation pair.

**Interpretation**: Higher scores indicate better performance in commonsense reasoning by assessing the ability to select correct translations based on commonsense knowledge.

**Baseline Results**: Transformer model achieves a highest accuracy of 0.712 on the test suite.

**Validation**: Extensive experiments conducted with analyses to evaluate the reasoning capability of neural machine translation models on the test suite.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
