# What can AI do for me? Evaluating Machine Learning Interpretations in Cooperative Play

## 📊 Benchmark Details

**Name**: What can AI do for me? Evaluating Machine Learning Interpretations in Cooperative Play

**Overview**: We propose an evaluation of interpretation on a real task with real human users, where the effectiveness of interpretation is measured by how much it improves human performance. We design a grounded, realistic human-computer cooperative setting using a question answering task, Quizbowl. We recruit both trivia experts and novices to play this game with computer as their teammate, who communicates its prediction via three different interpretations. We also provide design guidance for natural language processing human-in-the-loop settings.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing
- Human-Computer Interaction

**Resources**:
- [Resource](https://doi.org/10.1145/3301275.3302265)
- [Resource](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-highlighting.html)
- [Resource](https://youtu.be/bYFqMINXayc)

## 🎯 Purpose and Intended Users

**Goal**: Measure interpretability by asking what machine learning can do for humans through interpretations: interpretations should augment human intelligence and improve human performance on a real task (Quizbowl).

**Target Audience**:
- Natural Language Processing researchers
- Designers of human-in-the-loop systems
- Human-Computer Interaction researchers

**Tasks**:
- Question Answering
- Evaluation of interpretability (human-in-the-loop)

**Limitations**: Fixed placement of visualizations leads to uneven exposure; randomization of visualizations may confuse users; cannot derive causality from correlation in results; attention to visualizations not measured (eye tracking absent); suggested need for warm-up questions and further interface tuning.

## 💾 Data

**Source**: 160 new Quizbowl questions collected by the authors that had not been previously seen by the Quizbowl community.

**Size**: 160 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Application-grounded human evaluation (real users performing a real task)
- Controlled randomized exposure of interpretation conditions (2x2x2 = 8 conditions)
- Within-subjects design
- Regression analysis using a linear model trained on gameplay data

**Metrics**:
- Accuracy
- Average buzzing position (relative to question length)
- Regression coefficients of the linear model (effect sizes for features/interpretations)

**Calculation**: For each gameplay record, features (player ID, question ID, interpretation combination, buzzing position, and expert-setting features where applicable) are extracted and fed into a linear model which predicts probability of a correct answer; the model is trained with gradient descent on gameplay data. Coefficients indicate the effect of each feature/interpretation on the probability of a correct answer.

**Interpretation**: Positive regression coefficients indicate that an interpretation improves player accuracy; negative coefficients indicate the interpretation hurts accuracy. Earlier buzzing position indicates greater aggressiveness; ideal behavior is answering correctly with as few words as possible.

**Validation**: Randomized sampling of interpretation combinations to achieve, in expectation, a uniform distribution over players, questions, and interpretation combinations; separate analyses for experts and novices; tutorial provided to users prior to experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Robustness
- Value Alignment
- Data Laws
- Explainability

**Atlas Risks**:
- **Fairness**: Decision bias
- **Transparency**: Lack of training data transparency
- **Robustness**: Evasion attack
- **Value Alignment**: Over- or under-reliance
- **Data Laws**: Data usage restrictions
- **Explainability**: Untraceable attribution

**Demographic Analysis**: Comparison between two participant groups: experts (Quizbowl enthusiasts) and novices (Amazon Mechanical Turk workers); analyses report differences in accuracy, buzzing position, and sensitivity to interpretations.

**Potential Harm**: ['Over-reliance on model predictions leading to incorrect decisions (novices trusting misleading interpretations)', 'False sense of security from unfaithful or fragile interpretations', 'Decision bias in high-risk decision-making domains due to insufficient interpretability']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants were not asked for identifying information other than an optional email address for prize collection; online play platforms are usually anonymous.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
