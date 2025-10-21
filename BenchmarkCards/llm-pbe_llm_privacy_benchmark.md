# LLM-PBE (LLM Privacy BEnchmark)

## 📊 Benchmark Details

**Name**: LLM-PBE (LLM Privacy BEnchmark)

**Overview**: LLM-PBE is a toolkit designed for the systematic evaluation of data privacy risks in Large Language Models (LLMs), analyzing privacy across the entire lifecycle of LLMs, incorporating diverse attack and defense strategies, and handling various data types and metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://llm-pbe.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide an in-depth systematization of privacy risks associated with LLMs and enable systematic evaluation of privacy vulnerabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Data Privacy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Data used in experiments includes datasets like Enron emails, ECHR legal cases, and Python code from GitHub repositories.

**Size**: 500,000 emails for Enron, 11,500 cases for ECHR, 10.5GB of text from 22,133 GitHub repositories

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Data extraction accuracy
- Membership Inference Attack AUC
- Jailbreaking success rate

**Calculation**: Metrics are calculated based on the successful extraction of training data and other evaluation approaches.

**Interpretation**: Higher accuracy indicates greater privacy risk and vulnerability in the models.

**Baseline Results**: N/A

**Validation**: Extensive experimentation with multiple LLMs to assess the privacy of training data and prompt leakage.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The toolkit evaluates privacy risks without exposing sensitive information.

**Data Licensing**: This work is licensed under the Creative Commons BY-NC-ND 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
