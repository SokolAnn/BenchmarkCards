# BESPOKE (Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback)

## 📊 Benchmark Details

**Name**: BESPOKE (Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback)

**Overview**: BESPOKE is a realistic benchmark designed for evaluating personalization in search-augmented LLMs, constructed from authentic user history sessions and human-annotated preference scores and feedback.

**Data Type**: chat and search history pairs with preference annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LaMP-QA

**Resources**:
- [Resource](https://augustinlib.github.io/BESPOKE/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate personalization in search-augmented LLMs and provide a clear framework for benchmarking their effectiveness in understanding and adapting to user preferences.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Information Retrieval
- Personalization Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Created through long-term human annotation involving active daily use of chat and search systems by diverse user profiles.

**Size**: 2,870 user history sessions

**Format**: JSON

**Annotation**: Manual annotation by human annotators who provided feedback on the responses generated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Response-Judgment pair annotations

**Metrics**:
- Need Alignment
- Content Depth
- Tone
- Explanation Style

**Calculation**: Calculated using a 5-point Likert scale based on human annotator ratings.

**Interpretation**: Higher scores indicate better alignment of model responses with user needs and preferences.

**Baseline Results**: N/A

**Validation**: Validated through comparisons with existing benchmarks and qualitative assessments by human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User histories were de-identified and handled to ensure no personally identifiable information is disclosed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all human annotators prior to participation.

**Compliance With Regulations**: The study follows ethical standards for data protection and privacy.
