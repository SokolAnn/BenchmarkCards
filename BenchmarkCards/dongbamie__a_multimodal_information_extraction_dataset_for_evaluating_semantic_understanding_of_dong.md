# DongbaMIE: A Multimodal Information Extraction Dataset for Evaluating Semantic Understanding of Dongba Pictograms

## 📊 Benchmark Details

**Name**: DongbaMIE: A Multimodal Information Extraction Dataset for Evaluating Semantic Understanding of Dongba Pictograms

**Overview**: DongbaMIE is the first dataset focusing on multimodal information extraction of Dongba pictographs, consisting of images of Dongba hieroglyphic characters and their corresponding semantic annotations in Chinese, containing 23,530 sentence-level and 2,539 paragraph-level high-quality text-image pairs.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Cultural Heritage

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/thinklis/DongbaMIE)

## 🎯 Purpose and Intended Users

**Goal**: To improve the semantic understanding of Dongba hieroglyphs and facilitate research in multimodal information extraction.

**Target Audience**:
- ML Researchers
- Cultural Heritage Scholars
- NLP Practitioners

**Tasks**:
- Multimodal Information Extraction

**Limitations**: The dataset is limited to the first ten volumes of the Annotated Collection of Naxi Dongba Manuscripts.

## 💾 Data

**Source**: Annotated Collection of Naxi Dongba Manuscripts (He et al., 1999)

**Size**: 23,530 sentence-level and 2,539 paragraph-level pairs

**Format**: JSON

**Annotation**: Manually annotated by trained experts with a focus on semantic dimensions: object, action, relation, and attribute.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model performance in extracting objects, actions, relations, and attributes from the data.

**Interpretation**: Higher scores indicate better performance in extracting semantic information accurately.

**Validation**: The dataset was validated through a multi-tiered quality assurance mechanism and inter-annotator agreement evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The dataset includes demographic annotations pertaining to the Naxi ethnic group.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
