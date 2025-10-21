# MTalk-Bench

## 📊 Benchmark Details

**Name**: MTalk-Bench

**Overview**: MTalk-Bench is a multi-turn speech-to-speech benchmark designed for holistic evaluation of speech-to-speech large language models in complex dialogues, targeting three core dimensions: Semantic Information, Paralinguistic Information, and Ambient Sound, with a dual-method evaluation framework.

**Data Type**: multi-turn audio dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VoiceBench
- VoxDialogue
- SUPERB

**Resources**:
- [Resource](https://freedomintelligence.github.io/MTalk-Bench/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of speech-to-speech models across semantic understanding, paralinguistic expression, and ambient sound processing in multi-turn dialogues.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Dialogue Understanding
- Emotion Recognition
- Context Awareness

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset from human and model-generated dialogues, augmented with paralinguistic and ambient sound tags.

**Size**: Over 1,500 dialogue instances

**Format**: Audio recordings

**Annotation**: Manually annotated for semantic accuracy and paralinguistic features by expert annotators.

## 🔬 Methodology

**Methods**:
- Arena-style evaluation
- Rubric-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Elo scoring for pairwise comparisons, with refinement through human feedback and rubric metrics.

**Interpretation**: Scores indicate the effectiveness of models in capturing high-quality spoken dialogues and handling contextual variables.

**Baseline Results**: N/A

**Validation**: Evaluations conducted with both human and automated judges across multiple scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
