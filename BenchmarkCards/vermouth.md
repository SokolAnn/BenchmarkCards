# VerMouth

## 📊 Benchmark Details

**Name**: VerMouth

**Overview**: VerMouth is the first large-scale dataset comprising roughly 12 thousand claim-response pairs linked to debunking articles, accounting for both social media-style and basic emotions. It aims to automate fact-checking through engaging responses to misinformation on social media platforms.

**Data Type**: claim-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FEVER
- SciFact
- COVID-fact

**Resources**:
- [GitHub Repository](https://github.com/marcoguerini/VerMouth)

## 🎯 Purpose and Intended Users

**Goal**: To counter misinformation by generating personalized explanations that engage social media users.

**Target Audience**:
- ML Researchers
- Academic Researchers
- Industry Practitioners

**Tasks**:
- Fact-Checking
- Explanation Generation

**Limitations**: Limited to English language only; covers a specific style of language commonly seen on certain social media platforms.

## 💾 Data

**Source**: Claims derived from FullFact articles.

**Size**: 12,000 examples

**Format**: JSON

**Annotation**: Annotated through an author-reviewer pipeline combining Large Language Models (LLMs) and human input.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- METEOR
- BERTScore
- BARTScore

**Calculation**: Metrics calculated based on the overlap between generated and reference texts.

**Interpretation**: Higher scores indicate better quality of generated responses.

**Validation**: Evaluated through both automatic and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is collected in a manner that avoids privacy concerns, as no real social media data is utilized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
