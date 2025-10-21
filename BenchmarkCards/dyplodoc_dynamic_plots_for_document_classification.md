# DYPLODOC (Dynamic Plots for Document Classification)

## 📊 Benchmark Details

**Name**: DYPLODOC (Dynamic Plots for Document Classification)

**Overview**: This paper proposes a dataset consisting of plot descriptions for thirteen thousand TV shows, along with meta-information and dynamic plots extracted from them to facilitate narrative analysis and generation tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AnastasiaMalysheva/dyplodoc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset of longer storylines that could be used for narrative research and demonstrate how the notion of the narrative arc could be applied to longer texts.

**Target Audience**:
- ML Researchers
- Narrative Analysts

**Tasks**:
- Narrative Analysis
- Story Generation

**Limitations**: N/A

## 💾 Data

**Source**: TVmaze dataset accessed via the TVmaze API.

**Size**: 13,813 TV shows and 21,962 seasons consisting of more than 300,000 episodes

**Format**: N/A

**Annotation**: Condensed descriptions of main storylines and annotated genres.

## 🔬 Methodology

**Methods**:
- Dynamic Plot Extraction
- Clustering with K-means

**Metrics**:
- Mutual Information

**Calculation**: Comparison of cluster dynamics with static genre tags for seasons.

**Interpretation**: Higher mutual information indicates better alignment of dynamic plot features with static genre labels.

**Baseline Results**: N/A

**Validation**: Validation conducted through clustering analysis and comparison with static information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
