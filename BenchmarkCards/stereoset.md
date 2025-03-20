# StereoSet

## 📊 Benchmark Details

**Name**: StereoSet

**Overview**: A large-scale natural English dataset to measure stereotypical biases in four domains: gender, profession, race, and religion.

**Data Type**: Natural language

**Domains**:
- Gender
- Profession
- Race
- Religion

**Languages**:
- English

**Similar Benchmarks**:
- CrowS-Pairs
- WEAT
- SEAT

**Resources**:
- [Resource](https://stereoset.mit.edu)

## 🎯 Purpose and Intended Users

**Goal**: To measure and quantify the stereotypical biases present in pretrained language models.

**Target Audience**:
- Researchers
- AI practitioners

**Tasks**:
- Analyzing biases in language models
- Comparing models based on bias and language modeling ability

**Limitations**: Does not mitigate bias.

**Out of Scope Uses**:
- Training models on StereoSet
- Bias mitigation strategies

## 💾 Data

**Source**: Amazon Mechanical Turk

**Size**: 16,995 test instances

**Format**: Triplet format consisting of target context and associated attributes

**Annotation**: All instances validated by multiple crowdworkers

## 🔬 Methodology

**Methods**:
- Intrasentence Context Association Test (CAT)
- Intersentence Context Association Test (CAT)

**Metrics**:
- Language Modeling Score (lms)
- Stereotype Score (ss)
- Idealized CAT Score (icat)

**Calculation**: Calculate the percentage of instances preferring meaningful over meaningless associations and stereotypical over anti-stereotypical associations.

**Interpretation**: Higher lms indicates better language modeling ability while lower ss indicates less stereotypical bias.

**Validation**: Crowdsourced validation by 5 validators classifying associations

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in AI systems
- Misuse of bias data

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Societal Impact**: Impact on cultural diversity, Impact on education: plagiarism

**Demographic Analysis**: Crowdworkers were sourced from the USA.

**Potential Harm**: Promoting stereotypes and biases through model deployment.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: All workers were informed that their work would be used for a scientific study.

**Compliance With Regulations**: Workers were compensated at a minimum rate of $15 per hour, complying with AMT policies.
