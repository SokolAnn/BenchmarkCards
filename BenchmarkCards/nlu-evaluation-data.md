# NLU-Evaluation-Data

## 📊 Benchmark Details

**Name**: NLU-Evaluation-Data

**Overview**: A large, multi-domain (21 domains) dataset of 25K user utterances collected and annotated with Intent and Entity Type specifications; released alongside a systematic, wide-coverage evaluation and comparison of popular NLU services (Rasa, Watson, LUIS, Dialogflow).

**Data Type**: text (user utterances annotated with Intent and Entity Type labels)

**Domains**:
- alarm
- audio
- audiobook
- calendar
- cooking
- datetime
- email
- game
- general
- IoT
- lists
- music
- news
- podcasts
- general Q&A
- radio
- recommendations
- social
- food takeaway
- transport
- weather

**Similar Benchmarks**:
- Evaluating Natural Language Understanding Services for Conversational Question Answering Systems
- Benchmarking Natural Language Understanding Systems

**Resources**:
- [GitHub Repository](https://github.com/xliuhw/NLU-Evaluation-Data)
- [Resource](https://arxiv.org/abs/1903.05566)

## 🎯 Purpose and Intended Users

**Goal**: Provide a systematic, wide-coverage evaluation of commonly used NLU services and release a large, multi-domain dataset annotated with Intents and Entity Types to support unbiased comparison.

**Target Audience**:
- Conversational AI companies
- Industry practitioners
- Academic researchers

**Tasks**:
- Intent Classification
- Named Entity Recognition

**Limitations**: Dataset is unbalanced across Intents and Entities; contains noisy Entity annotations and annotation ambiguities; evaluation did not consider multiple intents per utterance or use of dialogue context; Watson's recent 'Contextual Entity' feature was not evaluated.

## 💾 Data

**Source**: Collected via Amazon Mechanical Turk (AMT) using scenario-driven prompts for a home assistant robot covering 21 domains (alarm, audio, audiobook, calendar, cooking, datetime, email, game, general, IoT, lists, music, news, podcasts, general Q&A, radio, recommendations, social, food takeaway, transport, weather).

**Size**: 25,716 utterances

**Format**: CSV (original); converted to platform-specific JSON formats for Rasa, Dialogflow, LUIS and Watson

**Annotation**: Annotated for Intent (predetermined set of 64 Intents) and Entity Tokens & Entity Types by three student annotators; inter-annotator agreement measured with Fleiss's Kappa (κ = 0.69). Partial token matching counted as match when entity tokens overlapped and entity types matched exactly.

## 🔬 Methodology

**Methods**:
- Automated metrics (Precision, Recall, F1)
- 10-fold cross-validation
- Statistical significance testing (pairwise t-tests, Cohen's D)

**Metrics**:
- Precision
- Recall
- F1 Score
- Micro-average

**Calculation**: Micro-average: sums up the individual True Positives, False Positives, and False Negatives of all Intent/Entity classes to compute the average metric (as used in the paper).

**Interpretation**: Higher Precision/Recall/F1 indicate better performance; Intent and Entity Type recognition were evaluated separately and combined. Statistical tests (pairwise t-tests) used to assess significance of differences; Cohen's D reported for effect size.

**Baseline Results**: Intent F1 scores (micro-average): Rasa 0.863, Dialogflow 0.864, LUIS 0.855, Watson 0.882. Entity F1 scores (micro-average): Rasa 0.768, Dialogflow 0.743, LUIS 0.777, Watson 0.488. Combined overall (Intent+Entity) F1: Rasa 0.822, Dialogflow 0.811, LUIS 0.821, Watson 0.657.

**Validation**: 10-fold cross-validation on a sub-corpus of 11,036 utterances (190 instances per intent where possible); detailed confusion matrices provided; annotation reliability measured with Fleiss's Kappa (κ = 0.69).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Data contamination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
