# CrossWOZ

## 📊 Benchmark Details

**Name**: CrossWOZ

**Overview**: CrossWOZ is a large-scale Chinese cross-domain (multi-domain) Wizard-of-Oz task-oriented dialogue dataset intended to advance multi-domain dialogue modeling and alleviate the shortage of Chinese task-oriented datasets. It contains 6K dialogue sessions and 102K utterances across 5 domains (hotel, restaurant, attraction, metro, and taxi), with rich annotation of dialogue states and dialogue acts on both user and system sides. About 60% of dialogues have cross-domain user goals. The authors provide a user simulator and several benchmark models for pipelined task-oriented dialogue system components.

**Data Type**: text (task-oriented dialogue sessions: user and system utterances; dialogue states and dialogue acts)

**Domains**:
- Natural Language Processing
- Tourism

**Languages**:
- Chinese

**Similar Benchmarks**:
- MultiWOZ
- Schema

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/CrossWOZ)

## 🎯 Purpose and Intended Users

**Goal**: To provide the first large-scale Chinese cross-domain task-oriented dialogue dataset to advance multi-domain (cross-domain) dialogue modeling and alleviate the shortage of Chinese task-oriented datasets.

**Target Audience**:
- Researchers
- Model developers

**Tasks**:
- Natural Language Understanding
- Dialogue State Tracking
- Dialogue Policy Learning
- Natural Language Generation
- User Simulation

**Limitations**: N/A

## 💾 Data

**Source**: Travel information for Beijing was crawled from the Web to build databases for Hotel, Attraction, and Restaurant domains; metro information was derived from HAR entities to build the metro database; taxi domain uses pseudo car type and plate number. Dialogues were collected via a synchronous human-to-human Wizard-of-Oz setting on a specialized website where well-trained workers (90 workers) were paired to converse according to generated multi-domain goals; workers also annotated user states and system states. Dialogue acts and states were further annotated automatically by rules and evaluated by three experts on a sample.

**Size**: 6,012 dialogues total (5,012 training / 500 validation / 500 test); ~102,000 utterances. Training turns: 84,692; Validation turns: 8,458; Test turns: 8,476. Tokens: 1,376,033 (train) / 137,736 (valid) / 137,427 (test).

**Format**: N/A

**Annotation**: Dialogue acts and dialogue states annotated automatically using rule-based methods derived from user/system states and keyword matching; each utterance can have multiple dialogue acts (intent, domain, slot, value). Three experts manually annotated 50 dialogues (806 utterances) for quality evaluation. Additional binary labels for semantic tuples indicating whether selected by user are provided.

## 🔬 Methodology

**Methods**:
- Automated metrics (corpus-based component evaluation)
- User simulation (system-level evaluation using provided rule-based user simulator)

**Metrics**:
- F1 Score (Dialogue act F1)
- Joint State Accuracy (percentage of exact matching)
- BLEU Score (corpus-level BLEU)
- Task finish rate
- Dialogue act F1 (delexicalized)
- State accuracy

**Calculation**: Joint state accuracy is computed as the percentage of exact matching between predicted and gold system states. Corpus-level BLEU is computed using all utterances with the same delexicalized dialogue acts as references (about 100 references on average). Task finish is defined as when all slots in a user goal are filled by real values (simulation terminates). Dialogue act F1 and state accuracy follow standard definitions comparing predicted annotations to gold annotations.

**Interpretation**: Higher metric scores indicate better component/system performance. The paper interprets substantially lower scores on cross multi-domain dialogues (CM and CM+T) as indicating these tasks are more challenging. The paper notes that 'task finish' does not necessarily mean task success because the system may provide incorrect information.

**Baseline Results**: Provided benchmark model results (selected overall numbers): BERTNLU Dialogue act F1 (overall) = 95.53. RuleDST Joint state accuracy (single turn, overall) = 71.33. TRADE Joint state accuracy (overall) = 36.08. SL policy Dialogue act F1 (overall) = 44.92; delexicalized Dialogue act F1 (overall) = 66.02. TemplateNLG BLEU (user-side) = 0.5780; SC-LSTM BLEU (user-side) = 0.7858. System-level simulation task finish rates (overall): DA Sim = 34.6%, NL Sim (Template) = 23.6%, NL Sim (SC-LSTM) = 19.7%. (See paper Table 8 for per-goal-type breakdowns.)

**Validation**: Annotation quality evaluated by three experts on 50 dialogues (806 utterances). Agreement between experts: average dialogue act F1 = 94.59% and average state accuracy = 93.55%. Compared with each expert as gold standard: average dialogue act F1 = 95.36% and average state accuracy = 94.95%. Workers performed small pilot dialogues with feedback before formal collection; 90 well-trained workers participated in data collection.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
