# SMolInstruct

## 📊 Benchmark Details

**Name**: SMolInstruct

**Overview**: SMolInstruct is a large-scale instruction tuning dataset centering around small molecules. It contains 14 chemistry tasks and over 3 million rigorously curated samples, aiming to advance the performance of large language models (LLMs) in chemistry tasks.

**Data Type**: query-response pairs

**Domains**:
- Natural Language Processing
- Chemistry

**Languages**:
- English

**Similar Benchmarks**:
- Mol-Instructions

**Resources**:
- [Resource](https://osu-nlp-group.github.io/LLM4Chem/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research and applications in chemistry by providing a comprehensive dataset for instruction tuning of large language models.

**Target Audience**:
- ML Researchers
- Chemistry Researchers
- Model Developers

**Tasks**:
- Name Conversion
- Property Prediction
- Molecule Captioning
- Molecule Generation
- Forward Synthesis
- Retrosynthesis

**Limitations**: Despite high-quality curation, the dataset may still contain inaccuracies or be limited in assessing correctly generated descriptions or molecules.

## 💾 Data

**Source**: Various sources including PubChem, MoleculeNet, and USPTO-full.

**Size**: 3,288,855 samples

**Format**: JSON

**Annotation**: Curated and quality-controlled by experts and checks for molecular validity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Fingerprint Tanimoto Similarity (FTS)
- METEOR score
- Root Mean Square Error (RMSE)
- Accuracy

**Calculation**: Metrics calculated based on the proportion of correct predictions and structural similarities.

**Interpretation**: Higher values for metrics like EM, Accuracy indicate better performance, while lower RMSE signifies improved predictions.

**Baseline Results**: SoTA task-specific models outperform LlaSMol models on most tasks, but LlaSMol demonstrates notable improvements.

**Validation**: Rigorous quality control applied during data collection and before model training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
