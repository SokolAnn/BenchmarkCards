# HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems

## 📊 Benchmark Details

**Name**: HalluDetect: Detecting, Mitigating, and Benchmarking Hallucinations in Conversational Systems

**Overview**: HalluDetect is an LLM-based hallucination detection system that optimizes the performance of consumer grievance chatbots by benchmarking various architectures to mitigate hallucinations in their outputs, helping enhance the trustworthiness of AI assistants in high-risk domains.

**Data Type**: dialogue instances

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- HHEM v2
- LettuceDetect

**Resources**:
- [Resource](https://arxiv.org/abs/2509.11619)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of HalluDetect is to provide a scalable framework for hallucination detection and mitigation in consumer grievance chatbots, improving the reliability of AI-driven legal assistance tools.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Legal Experts
- Model Developers

**Tasks**:
- Hallucination Detection
- Text Generation
- Dialogue Management

**Limitations**: The effectiveness of HalluDetect has not been empirically validated across all potential domains; current evaluations are focused on legal and consumer grievance contexts.

## 💾 Data

**Source**: DetectorEval dataset consisting of 115 dialogue instances between chatbots and legal experts.

**Size**: 115 chat instances

**Format**: JSON

**Annotation**: Annotated for hallucination detection by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on detected hallucinations in multi-turn conversations across various chatbot architectures evaluated in the study.

**Interpretation**: A higher F1 Score indicates better performance in identifying hallucinations, with precision reflecting the correctness of identified hallucinated instances and recall indicating the thoroughness of detection.

**Baseline Results**: HalluDetect outperforms baseline detectors including LettuceDetect and HHEM v2, achieving significant improvements in both precision and recall rates.

**Validation**: HalluDetect was validated through extensive human evaluations of detected hallucinations in chatbot conversations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark includes demographic factors by addressing consumer grievance scenarios relevant in diverse consumer sectors.

**Potential Harm**: ['Misleading hallucinations affecting user trust in legal guidance.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets used contain synthetic or anonymized dialogues, ensuring no personally identifiable information is present.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
