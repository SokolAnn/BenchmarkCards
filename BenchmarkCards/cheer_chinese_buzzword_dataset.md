# CHEER (Chinese Buzzword Dataset)

## 📊 Benchmark Details

**Name**: CHEER (Chinese Buzzword Dataset)

**Overview**: CHEER is the first dataset of Chinese internet buzzwords, each annotated with a definition and relevant user-generated content (UGC) examples. This dataset is used to evaluate the performance of various definition generation methods, including a novel method called RESS.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/SCUNLP/Buzzword)

## 🎯 Purpose and Intended Users

**Goal**: To investigate if large language models can generate accurate definitions for Chinese internet buzzwords based on user-generated content and to benchmark existing definition generation methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- NLP Researchers

**Tasks**:
- Definition Generation
- Text Classification

**Limitations**: The overall performance of existing methods remains suboptimal, indicating room for improvement in handling the dynamic nature of internet buzzwords.

## 💾 Data

**Source**: User-generated content collected from social media platforms, including Xiaohongshu and Weibo, as well as definitions sourced from online dictionary platforms specializing in trending buzzwords.

**Size**: 1,127 buzzwords

**Format**: JSON

**Annotation**: Buzzwords were annotated with definitions and user-generated content examples, with a quality control process involving manual reviews.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Semantic Accuracy (SA)
- Semantic Completeness (SC)
- BLEU
- ROUGE-L (R-L)
- BERTScore (BScore)

**Calculation**: Metrics were calculated using automatic evaluations based on generated definitions and their comparisons to reference definitions, combined with human evaluations for semantic accuracy and completeness.

**Interpretation**: Good performance is indicated by high scores in semantic accuracy and completeness. Specific thresholds for acceptable performance were established through a combination of automated and human evaluations.

**Baseline Results**: Baseline methods include various existing definition generation techniques such as Direct Prompt, Chain-of-Thought, and FOCUS, with RESS showing performance improvements in semantic accuracy and completeness over these baselines.

**Validation**: The benchmark was validated using human evaluations and a contamination-free evaluation strategy to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: The dataset contains examples sourced from diverse user-generated content across major Chinese social media platforms, facilitating an understanding of demographic use in language.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is derived from anonymized, publicly available internet content, ensuring user privacy was maintained during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: No personally identifiable information was collected, adhering to ethical standards in data usage.

**Compliance With Regulations**: Not Applicable
