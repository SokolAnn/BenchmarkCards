# Review-Driven Multi-Label Music Style Classification

## 📊 Benchmark Details

**Name**: Review-Driven Multi-Label Music Style Classification

**Overview**: This paper explores a new natural language processing task, review-driven multi-label music style classification, which requires the system to identify multiple styles of music based on its reviews on websites. The authors build a new dataset and propose a label-graph based neural network and a soft training mechanism to learn and exploit style correlations.

**Data Type**: text (user reviews and album titles with multi-label style annotations)

**Domains**:
- Natural Language Processing
- Music Information Retrieval

**Languages**:
- Chinese

**Resources**:
- [Resource](https://music.douban.com)
- [Resource](https://arxiv.org/abs/1808.07604)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset and evaluate methods for review-driven multi-label music style classification: identifying multiple music styles from user reviews and exploiting style correlations.

**Tasks**:
- Multi-Label Classification
- Text Classification
- Music Style Classification

**Limitations**: The method performs worse on styles with low frequency in the training set due to a highly imbalanced label distribution; difficulty distinguishing music styles that share many common elements and only subtly differ from each other; limited availability of audio data due to copyright.

## 💾 Data

**Source**: Collected from a popular Chinese music review website (https://music.douban.com). Each sample is defined as an album and includes the title, a set of human annotated styles, and associated user reviews sorted by time.

**Size**: 7,172 samples total; 5,020 training, 646 validation, 1,506 testing; over 287,000 reviews; over 3.6 million words; 22 style labels; each sample labeled with 2 to 5 styles; average 2.2 styles per sample; average 40 reviews per sample; average 12.4 words per review.

**Format**: N/A

**Annotation**: Human annotated styles (manual annotation)

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (comparison to baseline models)
- Visualization analysis

**Metrics**:
- Micro F1
- Macro F1
- One-Error
- Hamming Loss

**Calculation**: Macro F1 computes the metric independently for each label and then takes the average; Micro F1 aggregates the contributions of all labels to compute the average. One-Error evaluates the fraction of examples whose top-ranked label is not in the gold label set. Hamming Loss counts the fraction of wrong labels to the total number of labels.

**Interpretation**: Higher Micro F1 and Macro F1 indicate better performance. Lower One-Error and lower Hamming Loss indicate better performance. (Table legend: "+" indicates higher is better; "-" indicates lower is better.)

**Baseline Results**: Baselines and key results (from Table 2): LSTM: One-Error 30.5, Hamming Loss 0.089, Macro F1 33.0, Micro F1 53.9. Proposed method (HAN + LCM): One-Error 22.6, Hamming Loss 0.074, Macro F1 54.4, Micro F1 64.5.

**Validation**: A validation set of 646 samples was used to tune hyper-parameters and select the best parameters for test evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Data acquisition

**Atlas Risks**:
- **Data Laws**: Data acquisition restrictions
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
