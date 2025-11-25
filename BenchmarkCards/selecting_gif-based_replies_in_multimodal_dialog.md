# Selecting Gif-based Replies in Multimodal Dialog

## 📊 Benchmark Details

**Name**: Selecting Gif-based Replies in Multimodal Dialog

**Overview**: This paper introduces a new dataset of 1.56M text-gif conversation turns and a new multimodal conversational model PEPE THE KINGPRAWN for selecting gif-based replies.

**Data Type**: text-gif conversation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/xingyaoww/gif-reply)

## 🎯 Purpose and Intended Users

**Goal**: To analyze multimodal conversations and improve gif response selection in conversational AI.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multimodal Dialog
- Response Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Twitter responses to English-language tweets containing gifs and filtered to match common gifs on Giphy.

**Size**: 1,562,701 pairs

**Format**: N/A

**Annotation**: Manual filtering and matching of gifs with corresponding tweets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- nDCG

**Calculation**: nDCG measures whether more appropriate gif responses are ranked higher based on manual annotation scores.

**Interpretation**: Higher nDCG indicates better quality responses.

**Baseline Results**: PEPE model achieves an nDCG of 0.8145.

**Validation**: Evaluated through manual annotations and a randomized controlled trial.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Reinforcement of cultural stereotypes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
