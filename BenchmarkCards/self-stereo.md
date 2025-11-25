# Self-Stereo

## 📊 Benchmark Details

**Name**: Self-Stereo

**Overview**: Self-Stereo is a new dataset of self-reported stereotypes collected from Reddit, which links socio-demographic categories with stereotypical or non-stereotypical attributes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- SHADES

**Resources**:
- [Resource](https://osf.io/x7evc/)

## 🎯 Purpose and Intended Users

**Goal**: To investigate risks of persona-prompting in LLMs and analyze linguistic abstraction in relation to stereotypes.

**Target Audience**:
- ML Researchers
- Social Scientists
- Industry Practitioners

**Tasks**:
- Text Generation
- Bias Detection

**Limitations**: The dataset is collected from Reddit, which may not be fully representative of the entire population; only self-reported stereotypes are included.

## 💾 Data

**Source**: Collected from the Reddit post 'What stereotype is 100% accurate about you?'

**Size**: 867 comments

**Format**: JSON

**Annotation**: Three expert annotators labeled text-spans corresponding to socio-demographic categories and attributes.

## 🔬 Methodology

**Methods**:
- Statistical Analysis
- Interaction Experiments with LLMs

**Metrics**:
- Concreteness
- Specificity
- Negation

**Calculation**: Concreteness calculated from ratings of multiword expressions; specificity calculated from WordNet taxonomy; negation normalized by number of tokens.

**Interpretation**: Higher values indicate more biased and stereotyped descriptions; all texts remain abstract despite persona-prompting.

**Baseline Results**: LLMs show low ability to reproduce expected stereotypical associations accurately; various LLMs were evaluated.

**Validation**: Experimentation involved diverse prompt conditions and model sizes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Self-reported stereotypes included various socio-demographic categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data has been anonymized; no personally identifiable information is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
