# Meet Up! A Corpus of Joint Activity Dialogues in a Visual Environment

## 📊 Benchmark Details

**Name**: Meet Up! A Corpus of Joint Activity Dialogues in a Visual Environment

**Overview**: MeetUp! is a two-player coordination game where players move in a visual environment, with the objective of finding each other. To do so, they must talk about what they see, and achieve mutual understanding. The task requires both visual and conversational grounding and makes stronger demands on representations of the discourse.

**Data Type**: multimodal (text dialogues paired with room images)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Visual Dialogue
- GuessWhat?!
- PhotoBook Dataset
- HCRC Map Task Corpus
- Vision-and-Language Navigation

**Resources**:
- [GitHub Repository](https://github.com/clp-research/meetup)
- [Resource](https://arxiv.org/abs/1907.05084)

## 🎯 Purpose and Intended Users

**Goal**: To collect dialogues for a task (MeetUp!) that brings together visual grounding and conversational grounding, requiring stronger discourse representations; to provide a resource that challenges models to combine language and vision skills.

**Target Audience**:
- Machine Learning Researchers
- Computational Linguistics Researchers
- Linguistic Researchers

**Tasks**:
- Dialogue Understanding
- Visual Grounding
- Scene Categorization
- Navigation

**Limitations**: Uses a discrete variant of the game implemented as connected subgraphs of a two-dimensional grid (10 nodes) rather than continuous movement; initial collection size limited to 430 completed dialogues.

## 💾 Data

**Source**: Images sampled from the ADE20k corpus (Zhou et al., 2017); dialogues collected via the Slurk chat-tool deployed through Amazon Mechanical Turk.

**Size**: 430 completed dialogues (547 plays collected, 117 discarded); 5,695 turns; average dialogue length 13.2 turns (66.9 tokens); 2,983 word form types.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics (descriptive statistics over collected dialogues)
- Data collection via crowd-sourcing (Amazon Mechanical Turk) using the Slurk chat-tool

**Metrics**:
- Success Rate (proportion of completed dialogues where both players end in same room of correct type)
- Average number of turns per dialogue
- Average tokens per dialogue
- Number of turns
- Vocabulary size (word form types)
- MOVE/SAY ratio (navigation actions vs. SAY actions)
- Median time spent in a room
- Number of questions per dialogue
- Contribution ratio between players (tokens and turns)

**Calculation**: Success Rate: proportion of completed dialogues where both players end in same room of correct type (authors report 87%). Averages computed across completed dialogues (e.g., average length 13.2 turns; 66.9 tokens). Vocabulary overlap measured as intersection over union. MOVE/SAY ratio computed as number of navigation actions divided by number of SAY actions.

**Interpretation**: Results indicate the task leads to rich, natural and varied dialogue; high success rate (87%) shows participants can coordinate to meet the goal; dialogues exhibit phenomena (e.g., meta-semantic interaction, negotiation of classification decisions, discourse memory) that challenge existing language & vision datasets.

**Validation**: Plays where a player left prematurely or technical problems occurred were discarded (117 discarded out of 547). Success of a game is determined by both players issuing '/done' and indeed being in the same room of the target type.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: 126 distinct participants (AMT IDs); distribution of number of games per worker reported (most workers played more than one game); examples: most prolific worker participated in 49 games; in 22 games two novices played with each other, in 81 games one novice, in 305 games both players had played before.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
