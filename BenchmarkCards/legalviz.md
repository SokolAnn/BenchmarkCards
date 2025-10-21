# LegalViz

## 📊 Benchmark Details

**Name**: LegalViz

**Overview**: LegalViz is a novel dataset for visualizing legal texts through diagram generation, providing 7,010 pairs of legal documents and visualizations across 23 languages, utilizing the DOT graph description language of Graphviz.

**Data Type**: legal document and visualization pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Bulgarian
- Czech
- Danish
- Estonian
- French
- Hungarian
- Italian
- Latvian
- Lithuanian
- Maltese
- Dutch
- Polish
- Portuguese
- Romanian
- Slovak
- Slovenian
- Spanish
- Swedish

**Resources**:
- [GitHub Repository](https://github.com/mizuumi/LegalViz)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for legal text visualization, facilitating the understanding of complex legal documents for non-experts through diagrams.

**Target Audience**:
- ML Researchers
- Legal Professionals
- Natural Language Processing Practitioners

**Tasks**:
- Text Visualization
- Legal Entity Extraction
- Legal Relationship Representation

**Limitations**: The dataset may not perform equally across all 23 languages due to varying resource availability.

## 💾 Data

**Source**: Legal documents sourced from the EUR-LEX website, including judgments, orders, and rules of EU countries.

**Size**: 7,010 pairs

**Format**: DOT language code

**Annotation**: Manually annotated by legal domain experts using the DOT language of Graphviz.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated by comparing generated diagrams to reference diagrams using alignment and textual similarity measures.

**Interpretation**: Higher scores indicate better alignment between generated visualizations and reference diagrams, reflecting the quality of both graph structure and legal content representation.

**Validation**: Dataset was validated through empirical studies comparing few-shot and fine-tuned models on legal diagram generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is based on publicly available EU legal materials, excluding personal or sensitive information.

**Data Licensing**: Licensed under the Creative Commons Attribution 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
