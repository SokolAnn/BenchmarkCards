# ViStoryBench

## 📊 Benchmark Details

**Name**: ViStoryBench

**Overview**: ViStoryBench is a comprehensive benchmark designed to evaluate story visualization models across diverse narrative structures, visual styles, and character settings. It features richly annotated multi-shot scripts derived from curated stories, facilitated by large language models and verified by humans for quality and consistency.

**Data Type**: multi-shot scripts with character references

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- VinaBench
- StoryBench

**Resources**:
- [Resource](https://vistorybench.github.io/story_detail)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ViStoryBench is to provide a high-fidelity and multi-dimensional evaluation framework for assessing the performance of story visualization models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Story Visualization Evaluation
- Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated stories from literature, film, and folklore.

**Size**: 80 stories with 1,317 shots and 509 reference images

**Format**: JSON

**Annotation**: Manual collection and AI generation, verified by human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User studies
- Analytical evaluations of model outputs

**Metrics**:
- Character consistency
- Style similarity
- Prompt adherence
- Aesthetic quality

**Calculation**: Metrics are calculated through automated evaluations and validated by human studies.

**Interpretation**: Scores are interpreted based on the models' ability to generate images that align with provided narratives and character descriptions.

**Baseline Results**: Comprehensive evaluations conducted on over 20 methods including open-source and commercial models.

**Validation**: Models are evaluated through a public leaderboard and user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: Demographic analysis is included to measure fairness across groups.

**Potential Harm**: ['Risk of reproducing stereotypes and amplifying data-driven biases.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
