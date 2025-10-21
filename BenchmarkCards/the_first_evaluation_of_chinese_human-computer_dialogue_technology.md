# The First Evaluation of Chinese Human-Computer Dialogue Technology

## 📊 Benchmark Details

**Name**: The First Evaluation of Chinese Human-Computer Dialogue Technology

**Overview**: Introduces the first evaluation of Chinese human-computer dialogue technology, detailing the evaluation scheme, tasks, metrics, and how to collect and annotate the data for training, developing and test. The evaluation includes two tasks: user intent classification and online testing of task-oriented dialogue. The evaluation data is provided by the iFLYTEK Corporation. The paper publishes evaluation results and analyzes existing problems of human-computer dialogue and the evaluation scheme.

**Data Type**: text (single-utterance user messages and ASR results; complete user-intent dialogues); structured JSON records (flight, train, hotel data files)

**Domains**:
- Natural Language Processing
- Human-Computer Interaction
- Speech Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](http://www.iflytek.com/en/index.html)

## 🎯 Purpose and Intended Users

**Goal**: To introduce and run the first evaluation of Chinese human-computer dialogue technology, present the evaluation scheme, tasks and metrics, release the evaluation corpus (from iFLYTEK) for training/development/testing, and publish evaluation results to present current performance and analyze existing problems.

**Target Audience**:
- Academia (researchers)
- Industry practitioners
- Dialogue system developers / participants

**Tasks**:
- User Intent Classification
- Online Testing of Task-oriented Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: All data for training, developing and test is provided by the iFLYTEK Corporation from their real online applications (as stated in the paper).

**Size**: Task 1: 4,000 examples (total across released categories, as shown in Table 3); Task 2: 11 examples of complete user intent and 3 data files containing about one month of flight, hotel and train information.

**Format**: JSON (flight/train/hotel data files for Task 2); format of Task 1 released data not specified in the paper.

**Annotation**: Data annotation performed/supported by the authors' research center and iFLYTEK staff (acknowledged). Specific annotation procedures are not detailed.

## 🔬 Methodology

**Methods**:
- Automated metrics (Task 1 F1-score)
- Manual human evaluation (Task 2 online testing with human testers)
- Online testing (real-time human-computer dialogues for Task 2)

**Metrics**:
- F1 Score
- Task completion ratio
- User satisfaction degree
- Response fluency
- Number of dialogue turns
- Guidance ability for out of scope input

**Calculation**: Task 1: F1-score used for user intent classification. Task 2: Task completion ratio = number of completed tasks / total number of tasks. User satisfaction degree: five scores {-2, -1, 0, 1, 2} corresponding to very dissatisfied, dissatisfied, neutral, satisfied, very satisfied. Response fluency: three scores {-1, 0, 1} indicating nonfluency, neutral, fluency. Number of dialogue turns: number of utterances in a task-completed dialogue; if a task is not completed within 30 turns it is ended and the number of turns is set to 30. Guidance ability for out of scope input: scores {0, 1} representing unable/able to guide.

**Interpretation**: For Task 1 higher F1 is better. For Task 2 higher task completion ratio and higher user satisfaction degree indicate better performance; fewer dialogue turns are better (the paper states the less number of turns, the better for a completed task). Response fluency and guidance ability are interpreted according to their score scales as defined.

**Baseline Results**: See paper Tables 4-6. Closed test Task 1 top F1: 0.9391 (Spoken Dialogue System Lab, South China Agricultural University). Open test Task 1 top F1: 0.9414 (Spoken Dialogue System Lab, South China Agricultural University). Task 2 results are provided in Table 6 (showing task completion ratio, satisfaction, fluency, turns, guide for submitted systems).

**Validation**: Task 1 uses a held-out test set (same test set for closed and open sub-tasks). Task 2 uses online human testers who start each system with the same initial sentence for a given complete user intent; human testers manually evaluate each system per the defined metrics. The paper reports participant and system submission counts (28 participants, 43 submitted systems for Task 1; 7 submitted systems for Task 2, 4 connected correctly).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
