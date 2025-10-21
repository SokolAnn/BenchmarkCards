# GraLMatch: Matching Groups of Entities with Graphs and Language Models

## 📊 Benchmark Details

**Name**: GraLMatch: Matching Groups of Entities with Graphs and Language Models

**Overview**: This paper introduces two new multi-source benchmark datasets for entity group matching, aimed at matching records originating from multiple data sources but representing the same real-world entities. It focuses on the concept of transitively matched records and proposes a novel methodology called GraLMatch to address the challenges in entity group matching.

**Data Type**: N/A

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/FernandoDeMeer/GraLMatch)

## 🎯 Purpose and Intended Users

**Goal**: To introduce the entity group matching task and the concept of transitively matched records while proposing a method that combines state-of-the-art pairwise EM models with GraLMatch.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Entity Matching

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dataset generated from Crunchbase records, modified to reflect real-world challenges in entity matching.

**Size**: 200,000 records

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- Cluster Purity Score

**Calculation**: Metrics are calculated based on the results of the matching process and the effectiveness of the proposed GraLMatch method.

**Interpretation**: Higher precision indicates a better ability to correctly assign records to groups without false positives.

**Baseline Results**: N/A

**Validation**: The methodology was validated through experiments on both real and synthetic datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from publicly available records; privacy measures included to anonymize sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
