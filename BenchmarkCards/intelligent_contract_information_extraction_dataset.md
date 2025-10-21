# Intelligent Contract Information Extraction Dataset

## 📊 Benchmark Details

**Name**: Intelligent Contract Information Extraction Dataset

**Overview**: The paper proposes a high-quality dataset construction method for complex contract information extraction tasks in industrial scenarios, improving model performance through automated annotation and data augmentation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://s3public.obei.com.cn/pbkton0002/platform/other/dasai/%E5%90%88%E5%90%8C%E4%BF%A1%E6%81%AF%E7%90%86%E8%A7%A3%E7%B3%BB%E7%BB%9F_%E8%B5%9A%E9%A2%98%E6%95%B0%E6%8D%AE.zip)

## 🎯 Purpose and Intended Users

**Goal**: To construct a large-scale, high-quality dataset of industrial contract texts and enhance the performance of large language models in contract information extraction tasks through fine-tuning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Obei Industrial Supply Chain Ecosystem Platform

**Size**: 10,000 qualification texts, 10,000 requirement texts

**Format**: N/A

**Annotation**: Automated annotation using GPT-4 and GPT-3.5 with clustering and stratified sampling methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Field Extraction Accuracy
- Field Recall
- Efficiency (contracts parsed per second)

**Calculation**: Field accuracy measures the hit rate of key fields predicted by the model. Field recall evaluates the coverage of structured content against true keys.

**Interpretation**: Higher accuracy, recall, and efficiency indicate improved performance in extracting contract information.

**Baseline Results**: Comparative evaluation against models such as GLM-4, Baichuan2, and Qwen.

**Validation**: Performance evaluation on training and testing datasets to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
