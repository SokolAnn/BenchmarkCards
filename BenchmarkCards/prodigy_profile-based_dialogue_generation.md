# PRODIGy (PROfile-based DIalogue Generation)

## 📊 Benchmark Details

**Name**: PRODIGy (PROfile-based DIalogue Generation)

**Overview**: PRODIGy is a dialogue generation dataset that integrates diverse profile representations to enhance the consistency and coherence of dialogue agents. It includes over 20,000 dialogues sourced from movie scripts with aligned speaker representations encompassing communication style, biography, personality, and gender.

**Data Type**: dialogue

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Persona-Chat

**Resources**:
- [GitHub Repository](https://github.com/LanD-FBK/prodigy-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that will facilitate the development of dialogue agents capable of maintaining consistent and coherent interactions by incorporating profile information.

**Target Audience**:
- ML Researchers
- Dialogue Systems Developers
- Industry Practitioners

**Tasks**:
- Dialogue Generation

**Limitations**: The dataset contains fictional characters, which may lead to stereotyped roles.

## 💾 Data

**Source**: Cornell Movie Dialogs Corpus

**Size**: 20,850 dialogues

**Format**: CSV

**Annotation**: Character profiles were annotated using a combination of crowd-sourced personality data and biographical information sourced from external websites.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Instruction prompting

**Metrics**:
- Conditional Perplexity
- Average Accuracy at N

**Calculation**: Metrics calculated based on the model's likelihood of generating a correct response given a dialogue history.

**Interpretation**: Lower perplexity and higher accuracy indicate better model performance.

**Validation**: Models were validated using both automatic evaluation metrics and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset may reflect biases in character representation since it utilizes roles from movie scripts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset avoids privacy concerns by using fictional characters instead of real users.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
