# DroidCall

## 📊 Benchmark Details

**Name**: DroidCall

**Overview**: DroidCall is the first training and testing dataset for accurate Android intent invocation, designed to enhance the capabilities of LLMs for mobile agents. It includes 10,000 samples of user instructions paired with corresponding intents, allowing models to effectively learn intent invocation.

**Data Type**: instruction-intent pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/UbiquitousLearning/DroidCall)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for fine-tuning LLMs for accurate intent invocation on Android devices.

**Target Audience**:
- ML Researchers
- Mobile Developers
- AI Practitioners

**Tasks**:
- Intent Invocation

**Limitations**: N/A

## 💾 Data

**Source**: Open-sourced dataset designed specifically for Android intent invocation.

**Size**: 10,000 examples

**Format**: JSON

**Annotation**: Automatically generated using a data generation pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Soft Accuracy

**Calculation**: Accuracy is calculated as the ratio of correctly predicted samples to the total number of samples. Soft Accuracy compares the proportion of accurately predicted parameters to the total number of parameters.

**Interpretation**: Accuracy determines the model's performance on matching function calls; higher accuracy indicates better performance in intent invocation.

**Baseline Results**: N/A

**Validation**: Evaluated using 200 test examples from the DroidCall dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['N/A']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is processed locally on devices to avoid data transmission risks.

**Data Licensing**: Open-sourced under a permissive license, specific details not provided in the paper.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
