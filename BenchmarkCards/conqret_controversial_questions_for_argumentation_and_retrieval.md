# ConQRet (Controversial Questions for Argumentation and Retrieval)

## 📊 Benchmark Details

**Name**: ConQRet (Controversial Questions for Argumentation and Retrieval)

**Overview**: ConQRet is a new benchmark featuring long and complex human-authored arguments on debated topics, grounded in real-world websites, allowing an exhaustive evaluation across retrieval effectiveness, argument quality, and groundedness.

**Data Type**: argument pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/emory-irlab/conqret-rag)

## 🎯 Purpose and Intended Users

**Goal**: To enable research on complex, evidence-based argumentation and improve automated evaluation methods for retrieval-augmented argumentation systems.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Argument Quality Evaluation
- Automated Metric Assessment

**Limitations**: N/A

## 💾 Data

**Source**: ProCon.org, a debate portal featuring controversial questions with expert-generated pro and con arguments.

**Size**: 6,500 documents and 98 topics

**Format**: JSON

**Annotation**: Human annotation for argument quality across multiple dimensions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation
- Human evaluation

**Metrics**:
- Argument Quality
- Context Relevance
- Groundedness

**Calculation**: Metrics are computed based on correlations with human evaluators and inter-annotator agreement.

**Interpretation**: Metrics indicate the effectiveness of retrieval and argument quality across various dimensions.

**Baseline Results**: Comparison with previous argumentation frameworks shows improved performance using LLM Judges.

**Validation**: Validated using both a prior dataset and the newly introduced ConQRet benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential biases in argument generation', 'Misinformation from retrieval sources']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
