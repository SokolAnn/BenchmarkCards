# DOLOMITES (Domain-Specific Long-Form Methodical Tasks)

## 📊 Benchmark Details

**Name**: DOLOMITES (Domain-Specific Long-Form Methodical Tasks)

**Overview**: DOLOMITES provides a benchmark with specifications for 519 methodical tasks elicited from experts across 25 fields, aimed at evaluating contemporary language models on their ability to assist in structured, methodical writing tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare
- Education
- Legal
- Engineering
- Environmental Science
- Journalism
- Psychology
- Sociology
- Visual Arts

**Languages**:
- English

**Resources**:
- [Resource](https://dolomites-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models in their ability to generate accurate and contextually relevant outputs for methodical writing tasks across various domains.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Generation
- Writing Assistance
- Methodical Task Completion

**Limitations**: N/A

## 💾 Data

**Source**: Task descriptions and examples elicited from experts in various fields, collected via surveys and expert annotations.

**Size**: 1,857 examples

**Format**: JSON

**Annotation**: Tasks were annotated by domain experts with extensive experience in each field.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Accuracy
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the comparison of generated outputs from language models against expert-generated reference outputs, evaluating their adherence to task structure and factual accuracy.

**Interpretation**: Performance is interpreted based on how well the models can follow task instructions and produce outputs that align with expert-level work.

**Baseline Results**: GPT-4 and other contemporary models were used as baseline comparisons to assess performance improvements.

**Validation**: The benchmark's validity was confirmed through independent assessments by field experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Exposing personal information

**Demographic Analysis**: Expert demographic breakdowns were analyzed to ensure representation across fields.

**Potential Harm**: ['Potential bias in generated outputs could perpetuate stereotypes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymity of participants and subjects is protected in data collection processes.

**Data Licensing**: The dataset is available under an open license to promote research and transparency.

**Consent Procedures**: Informed consent was obtained from all participants contributing to task elicitation.

**Compliance With Regulations**: Not Applicable
