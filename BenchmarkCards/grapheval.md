# GraphEval

## 📊 Benchmark Details

**Name**: GraphEval

**Overview**: A hallucination evaluation framework based on representing information in Knowledge Graph structures. It identifies specific triples in the KG that are prone to hallucinations, providing more insight into inconsistencies in LLM outputs.

**Data Type**: Text

**Domains**:
- Summarization
- Question Answering
- Common Sense Reasoning

**Languages**:
- English

**Similar Benchmarks**:
- FactScore
- G-Eval
- GPTScore

**Resources**:
- [Resource](arXiv:2407.10793v1)
- [Resource](Amazon Bedrock API)

## 🎯 Purpose and Intended Users

**Goal**: To improve the detection and correction of hallucinations in LLM outputs using a Knowledge Graph framework.

**Target Audience**:
- Researchers
- AI Developers
- Practitioners in Natural Language Processing

**Tasks**:
- Detect hallucinations in LLM outputs
- Provide explainable decisions on inconsistencies
- Correct identified hallucinations

**Limitations**: Focuses exclusively on closed-domain hallucination detection.

**Out of Scope Uses**:
- Open-domain hallucination detection
- Real-time applications without prior context

## 💾 Data

**Source**: SummEval, QAGS-C, QAGS-X datasets

**Size**: N/A

**Format**: Text

**Annotation**: Human-annotated for factual consistency

## 🔬 Methodology

**Methods**:
- Knowledge Graph construction
- Natural Language Inference models

**Metrics**:
- Balanced accuracy
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: Balanced accuracy calculated based on the number of factually consistent vs inconsistent examples.

**Interpretation**: Higher accuracy indicates better consistency between LLM output and provided context.

**Baseline Results**: Adding the GraphEval preprocessing step improved balanced accuracy by an average of 6.2 (SE=1.3).

**Validation**: Evaluated on popular hallucination detection benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Societal Impact
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on education: plagiarism, Impact on Jobs
- **Privacy**: Reidentification

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential job displacement due to automation in content generation', 'Educational integrity risks from reliance on LLMs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data is used in the evaluation datasets employed.

**Data Licensing**: Data is sourced from licensed datasets like CNN/DailyMail.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Follows ethical guidelines for handling generated data.
