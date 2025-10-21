# PLANTS (Planning-like Tasks)

## 📊 Benchmark Details

**Name**: PLANTS (Planning-like Tasks)

**Overview**: The PLANTS dataset is specifically designed for plan summarization tasks, encompassing diverse domains such as automated plans, recipes, and travel plans. It aims to generate concise and coherent summaries of action sequences that achieve specific goals.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/VishalPallagani/PLANTS-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in planning task summarization by providing a dataset specifically designed for summarizing planning-like (PL) tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Summarization

**Limitations**: The dataset includes only 10 problems per domain, which may not fully capture the variability and complexity of real-world planning tasks.

## 💾 Data

**Source**: The PLANTS dataset was created from automated plans sourced from the downward-benchmarks, recipes sourced from the Recipe1M+ dataset, and travel routes generated using the OpenStreetMap API.

**Size**: 130 plans

**Format**: N/A

**Annotation**: Data was manually curated and selected based on specific criteria to ensure diversity in the planning tasks.

## 🔬 Methodology

**Methods**:
- User studies
- Quantitative metrics

**Metrics**:
- Ease of understanding
- User preference scores

**Calculation**: Metrics were calculated based on user ratings and performance measures during evaluations.

**Interpretation**: Higher ratings in ease of understanding indicate better comprehension and quicker decision-making for the summaries.

**Baseline Results**: GPT-4o provided the highest ratings for ease of understanding across all PL tasks.

**Validation**: The human evaluation was conducted with inter-annotator agreement calculated using Cohen’s kappa coefficient.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data were sourced from publicly available repositories, ensuring compliance with usage terms and privacy regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Human evaluators participated voluntarily and provided informed consent.

**Compliance With Regulations**: Not Applicable
