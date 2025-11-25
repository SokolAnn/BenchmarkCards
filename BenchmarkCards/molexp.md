# MolExp

## 📊 Benchmark Details

**Name**: MolExp

**Overview**: MolExp is a novel benchmark emphasizing the discovery of structurally diverse molecules with similar bioactivity, simulating real-world drug design challenges.

**Data Type**: molecule similarity scores

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- GuacaMol

**Resources**:
- [GitHub Repository](https://github.com/MorganCThomas/MolScore)

## 🎯 Purpose and Intended Users

**Goal**: To measure the rediscovery of structurally diverse molecules with comparable bioactivity in drug design.

**Target Audience**:
- ML Researchers
- Drug Designers

**Tasks**:
- Molecule Exploration

**Limitations**: The benchmark relies on similarity functions that may not be used in real-world drug design.

## 💾 Data

**Source**: ChEMBL34 database

**Size**: 1,711,022 unique molecules

**Format**: SMILES

**Annotation**: Manual curation and filtering for drug-like properties.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Multi-Agent Learning

**Metrics**:
- Molecular Similarity
- Sphere Exclusion Diversity

**Calculation**: Molecular similarity is calculated using a modified scoring function based on Levenshtein distance.

**Interpretation**: A higher score indicates better performance in rediscovering target molecules.

**Baseline Results**: Baseline performance varies based on algorithm; ACEGEN MolOpt configuration performs best on tasks.

**Validation**: Benchmark performance validated with multiple runs and comparisons to existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
