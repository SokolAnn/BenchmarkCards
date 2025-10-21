# STATE ToxiCN (Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Detection)

## 📊 Benchmark Details

**Name**: STATE ToxiCN (Span-level Target-Aware Toxicity Extraction in Chinese Hate Speech Detection)

**Overview**: This paper presents the first span-level target-aware toxicity extraction dataset (STATE ToxiCN) designed for Chinese hate speech detection, which includes fine-grained annotations for identifying targets, arguments, and the associated hateful groups.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- COLD (Chinese Offensive Language Dataset)
- TOXICN

**Resources**:
- [GitHub Repository](https://github.com/shenmeyemeifashengguo/STATE-ToxiCN.detection)

## 🎯 Purpose and Intended Users

**Goal**: To advance the research on span-level hate speech detection in Chinese by providing a novel dataset and an annotated lexicon of hateful slang.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Hate Speech Detection
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from posts on online forums (Zhihu, Tieba) and includes manually annotated data.

**Size**: 8,029 posts and 9,533 Target-Argument-Hateful-Group quadruples

**Format**: JSON

**Annotation**: Manual annotation by experts with multi-stage quality control.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Macro-F1 Score

**Calculation**: Metrics are calculated using hard-matching and soft-matching criteria.

**Interpretation**: Higher F1 scores indicate better model performance in accurately detecting hateful speech.

**Baseline Results**: Results compared against baseline models like mT5, LLaMA3, and Shield models.

**Validation**: The dataset was validated through inter-annotator agreement metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes diverse demographic information of annotators to mitigate bias.

**Potential Harm**: The dataset aims to identify and mitigate harmful hate speech and its implications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain any personally identifiable information as per user privacy agreements.

**Data Licensing**: The dataset is licensed under Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license.

**Consent Procedures**: Informed consent procedures were implemented for annotators.

**Compliance With Regulations**: Not Applicable
