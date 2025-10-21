# COLD (Chinese Offensive Language Detection)

## 📊 Benchmark Details

**Name**: COLD (Chinese Offensive Language Detection)

**Overview**: COLD provides a benchmark and dataset for Chinese offensive language detection, assisting in maintaining a civilized environment on social media. It includes the COLD ATASET, which contains 37,480 comments categorized with offensive labels.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/COLDatasettask)

## 🎯 Purpose and Intended Users

**Goal**: To accelerate research in Chinese offensive language detection through a reliable and versatile benchmark.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Offensive Language Detection

**Limitations**: N/A

## 💾 Data

**Source**: Collected from social platforms including Zhihu and Weibo.

**Size**: 37,480 examples

**Format**: CSV

**Annotation**: Semi-automatically labeled with human verification in a model-in-the-loop setup.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Cross-entropy loss function used for training the offensive language detector.

**Interpretation**: Higher accuracy indicates better performance in detecting offensive language.

**Baseline Results**: COLD ETECTOR achieved 81% accuracy on the test set.

**Validation**: Validated through model-in-the-loop collection and inter-annotator agreement metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset is annotated with gender and regional backgrounds of annotators.

**Potential Harm**: ['Mislabeled data', 'Offensiveness induced by non-offensive prompts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected is publicly available and does not represent the authors' views.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
