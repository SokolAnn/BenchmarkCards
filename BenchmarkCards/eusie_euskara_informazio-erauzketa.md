# EusIE (Euskara Informazio-Erauzketa)

## 📊 Benchmark Details

**Name**: EusIE (Euskara Informazio-Erauzketa)

**Overview**: EusIE is the first Event Extraction benchmark for the Basque language, designed to evaluate the performance of cross-lingual transfer learning in Event Extraction tasks.

**Data Type**: event extraction data

**Domains**:
- Natural Language Processing

**Languages**:
- Basque
- English
- Spanish
- Portuguese
- Polish
- Turkish
- Hindi
- Japanese
- Korean

**Similar Benchmarks**:
- MEE (Multilingual Event Extraction)

**Resources**:
- [Resource](https://huggingface.co/datasets/HiTZ/EusIE)
- [GitHub Repository](https://github.com/MikelZubi/GrALAnswering)

## 🎯 Purpose and Intended Users

**Goal**: To present the first Basque Event Extraction benchmark and analyze the impact of linguistic typology on cross-lingual transfer quality.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Language Technologists

**Tasks**:
- Event Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Annotated from a snapshot of Basque Wikipedia focusing on events-related documents.

**Size**: 300 segments (1500 sentences)

**Format**: JSON

**Annotation**: Annotated by expert linguists.

## 🔬 Methodology

**Methods**:
- Cross-lingual transfer learning
- Sequence labeling

**Metrics**:
- F1 Score

**Calculation**: F1 scores calculated for each task using gold annotations.

**Interpretation**: Higher F1 scores indicate better transfer quality in event extraction tasks.

**Baseline Results**: N/A

**Validation**: Evaluated using cross-validation across multiple languages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
