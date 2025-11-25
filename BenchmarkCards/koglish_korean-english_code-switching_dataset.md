# Koglish (Korean-English Code-Switching Dataset)

## 📊 Benchmark Details

**Name**: Koglish (Korean-English Code-Switching Dataset)

**Overview**: The Koglish dataset is tailored for English-Korean code-switching scenarios, introducing Koglish-GLUE, Koglish-NLI, and Koglish-STS datasets to facilitate the study and evaluation of code-switching in natural language processing.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Korean

**Resources**:
- [Resource](https://huggingface.co/datasets/Jangyeong/Koglish_GLUE)
- [Resource](https://huggingface.co/datasets/Jangyeong/Koglish_STS)
- [Resource](https://huggingface.co/datasets/Jangyeong/Koglish_NLI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for studying and evaluating code-switching scenarios in English-Korean interaction and to enhance the effectiveness of multilingual models in such contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Natural Language Inference
- Semantic Textual Similarity

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using various language datasets with a focus on code-switching scenarios, using constituency parsing for dataset generation.

**Size**: Varies by sub-dataset; details available in the paper.

**Format**: N/A

**Annotation**: Manual evaluation by bilingual experts in Korean and English.

## 🔬 Methodology

**Methods**:
- Experimental evaluation using various multilingual models
- Contrastive Learning
- Data augmentation with code-switched sentences

**Metrics**:
- Accuracy
- Spearman’s correlation
- F1 Score

**Calculation**: Metrics calculated based on model performance outputs on the Koglish datasets.

**Interpretation**: Higher scores indicate better performance in understanding and processing code-switched sentences.

**Validation**: Performed with cross-validation using bilingual experts' evaluations.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
