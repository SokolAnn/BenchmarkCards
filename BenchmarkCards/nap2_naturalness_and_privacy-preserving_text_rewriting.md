# NAP2 (Naturalness and Privacy-Preserving Text Rewriting)

## 📊 Benchmark Details

**Name**: NAP2 (Naturalness and Privacy-Preserving Text Rewriting)

**Overview**: The NAP2 dataset focuses on naturalness and privacy-preserving methods for text rewriting, providing a corpus for researchers to develop and evaluate strategies for sanitizing sensitive text while maintaining privacy and utility.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve text rewriting techniques that maintain privacy while ensuring natural language quality.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Rewriting

**Limitations**: The dataset might not fulfill the expansive needs of commercial deployments due to its limited size.

## 💾 Data

**Source**: Curated from the open-domain dialogue corpus PERSONA-CHAT.

**Size**: 4,795 utterances

**Format**: N/A

**Annotation**: Human annotation and using large language models for synthetic data generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- PRIVACY_NLI
- ROUGE-1
- ROUGE-L

**Calculation**: Performance is evaluated based on the ability to retain privacy while preserving naturalness in rewrites.

**Interpretation**: Higher scores in metrics indicate better performance in privacy preservation and naturalness.

**Baseline Results**: Comparative evaluations showed superior performance of models fine-tuned on NAP2 over state-of-the-art methods and zero-shot LLMs.

**Validation**: Cross-validation procedures were used to ensure robust model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset focuses on ensuring anonymization of sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
