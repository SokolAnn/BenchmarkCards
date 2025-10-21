# T2VSafetyBench

## 📊 Benchmark Details

**Name**: T2VSafetyBench

**Overview**: T2VSafetyBench is a new benchmark designed for conducting safety-critical assessments of text-to-video models, addressing 12 critical aspects of video generation safety.

**Data Type**: malicious text prompts

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Vbench
- HEIM

**Resources**:
- [Resource](https://anonymous.4open.science/r/T2VSafetyBench_Code-1763/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the safety of text-to-video generative models by assessing their risk across multiple safety dimensions.

**Target Audience**:
- AI Researchers
- Safety Practitioners
- Model Developers

**Tasks**:
- Safety Assessment
- Risk Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Malicious text prompt dataset constructed from real-world prompts, generated prompts by GPT-4, and jailbreaking attack-based prompts.

**Size**: 4,400 prompts

**Format**: N/A

**Annotation**: Prompts curated and fine-tuned based on definitions of safety aspects.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated evaluation using GPT-4

**Metrics**:
- Correlation coefficient
- NSFW rate

**Calculation**: Correlation between GPT-4 assessments and human reviews is calculated to establish evaluation reliability.

**Interpretation**: A higher correlation coefficient indicates better alignment between automated and human assessments.

**Baseline Results**: N/A

**Validation**: The evaluation is validated through manual assessments by volunteers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained from volunteers for human evaluations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Volunteers were informed about the potential exposure to distressing content.

**Compliance With Regulations**: The study received exempt approval from the Institutional Review Board (IRB).
