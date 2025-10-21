# PolyMath

## 📊 Benchmark Details

**Name**: PolyMath

**Overview**: PolyMath is a multilingual mathematical reasoning benchmark covering 18 languages and 4 difficulty levels. It ensures comprehensive difficulty, language diversity, and high-quality translation, designed to evaluate the reasoning capabilities of advanced LLMs.

**Data Type**: mathematical problems

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Spanish
- Arabic
- French
- Bengali
- Portuguese
- Russian
- Indonesian
- German
- Japanese
- Swahili
- Vietnamese
- Italian
- Telugu
- Korean
- Thai
- Malay

**Similar Benchmarks**:
- MGSM
- MSVAMP
- MT-AIME

**Resources**:
- [GitHub Repository](https://github.com/QwenLM/PolyMath)
- [Resource](https://huggingface.co/datasets/Qwen/PolyMath)
- [Resource](https://Qwen-PolyMath.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PolyMath is to provide a benchmark for evaluating multilingual mathematical reasoning in the context of advanced LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 500 high-quality mathematical reasoning problems collected and translated into 18 languages, sourced from various educational and competitive mathematics repositories.

**Size**: 9000 problems

**Format**: Multiple-choice questions and structured mathematical problems

**Annotation**: Problems are annotated by experts in mathematics and linguistics to ensure high-quality translations and accurate difficulty assessment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Difficulty-Weighted Accuracy (DW-ACC)

**Calculation**: DW-ACC is calculated using level-specific weights for mathematical problems to address fairness in difficulty assessment across levels.

**Interpretation**: Higher DW-ACC scores indicate better overall reasoning performance across languages and difficulty levels.

**Baseline Results**: The benchmark was validated against several existing LLMs and evaluated for performance consistency across difficulty levels.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
