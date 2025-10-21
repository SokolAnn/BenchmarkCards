# SaTML (Secure and Trustworthy Machine Learning) Capture-the-Flag Competition Dataset

## 📊 Benchmark Details

**Name**: SaTML (Secure and Trustworthy Machine Learning) Capture-the-Flag Competition Dataset

**Overview**: The paper presents a dataset compiled from a capture-the-flag competition focused on leveraging Large Language Models (LLMs) to evaluate the security risks posed by prompt injection attacks. It contains over 137k multi-turn conversations documenting both defense strategies and attack attempts.

**Data Type**: multi-turn chat conversations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TensorTrust
- Gandalf

**Resources**:
- [Resource](https://huggingface.co/datasets/ethz-spylab/ctf-satml24)
- [GitHub Repository](https://github.com/ethz-spylab/ctf-satml24-data-analysis)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for studying prompt injection attacks and defenses in Large Language Models and to facilitate future research in LLM security.

**Target Audience**:
- ML Researchers
- Security Researchers
- Model Developers
- Educators

**Tasks**:
- Security Evaluation
- Model Benchmarking

**Limitations**: The dataset is specifically focused on secret extraction and may not represent broader tasks in language modeling.

## 💾 Data

**Source**: Collected during the IEEE SaTML 2024 CTF competition.

**Size**: 137,063 chats

**Format**: JSONL

**Annotation**: Dataset contains conversations tagged with success or failure of secret extraction.

## 🔬 Methodology

**Methods**:
- Automated metrics for evaluating defenses
- User-generated prompts for adaptive attacks

**Metrics**:
- Success rate of secret extraction
- Utility evaluation scores

**Calculation**: Scores are based on the number of attacks executed and the success of secret extraction across defenses.

**Interpretation**: Higher scores indicate more effective defenses and successful secret extractions.

**Validation**: The methodology was validated using utility evaluation metrics based on interaction results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Security

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants were informed that interactions would be public.

**Data Licensing**: Published under MIT License.

**Consent Procedures**: Participants agreed to the use of their interactions for research purposes.

**Compliance With Regulations**: Not Applicable
