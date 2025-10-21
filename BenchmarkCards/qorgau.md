# Qor´gau

## 📊 Benchmark Details

**Name**: Qor´gau

**Overview**: Qor´gau is a novel dataset specifically designed for safety evaluation in Kazakh and Russian, reflecting the unique bilingual context in Kazakhstan, where both Kazakh (a low-resource language) and Russian (a high-resource language) are spoken. It includes region-specific and culturally relevant prompts tailored for Kazakhstan.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Kazakh
- Russian

**Resources**:
- [GitHub Repository](https://github.com/mbzuai-nlp/qorgau-kaz-ru-safety)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety of large language models (LLMs) in bilingual contexts, specifically Kazakh and Russian, and to assess how LLMs handle risks unique to this region.

**Target Audience**:
- ML Researchers
- Safety Evaluators
- Model Developers

**Tasks**:
- Safety Evaluation
- Risk Assessment

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of region-specific prompts and questions developed specifically for Kazakh and Russian contexts, along with translations and localizations from other datasets.

**Size**: 8,000 prompts

**Format**: JSON

**Annotation**: Manually annotated by native speakers fluent in both languages.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Safety classification
- Human agreement rates

**Calculation**: Responses were classified as safe or unsafe based on risk-specific criteria, with evaluations performed by both humans and the GPT-4o model.

**Interpretation**: Safe responses are those that do not present harm and may include refusals or disclaimers, while unsafe responses contain harmful or misleading content.

**Baseline Results**: N/A

**Validation**: The framework utilized human evaluations to validate the reliability of automated assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
