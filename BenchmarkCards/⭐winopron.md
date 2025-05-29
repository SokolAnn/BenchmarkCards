# WinoPron

## 📊 Benchmark Details

**Name**: WinoPron

**Overview**: WinoPron is a new dataset created to address issues found in the original Winogender Schemas, focusing on evaluation of gender bias in coreference resolution systems with a corrected and more comprehensive set of templates. In addition to fixing typos and consistency issues, WinoPron explicitly balances for grammatical case, which has a dramatic effect on coreference resolution performance—a distinction often missed in prior work, where all cases were treated as equivalent for gender bias evaluation.

**Data Type**: Text

**Domains**:
- Coreference Resolution
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Winogender Schemas
- WinoBias
- WinoNB

**Resources**:
- [GitHub Repository](https://github.com/uds-lsv/winopron)
- [Paper](INSERT_PAPER_LINK_HERE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate gender bias in coreference resolution systems with a more reliable dataset that accounts for grammatical case and diverse pronoun usage.

**Target Audience**:
- Researchers in Natural Language Processing
- Coreference Resolution Developers

**Tasks**:
- Coreference resolution evaluation
- Gender bias measurement

**Limitations**: The dataset may not cover all linguistic variability in English; results may not generalize outside the evaluated pronoun sets and templates.

**Out of Scope Uses**:
- General text classification
- Non-English languages

## 💾 Data

**Source**: Original Winogender Schemas with additional and corrected templates.

**Size**: 1440 sentences

**Format**: Textual templates

**Annotation**: Templates verified for grammaticality, unique coreferences, and balanced grammatical case.

## 🔬 Methodology

**Methods**:
- Empirical evaluation of coreference resolution models
- Bias evaluation using a novel method that distinguishes grammatical case effects

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Measured across multiple pronoun sets and grammatical cases.

**Interpretation**: Understanding model performance based on grammatical case and pronoun set effects.

**Validation**: Automatic checks and human verification for grammaticality.

## ⚠️ Targeted Risks

**Risk Categories** (risks the dataset allows researchers to evaluate):
- Data bias in coreference resolution
- Evaluation consistency
- Data quality

**Dataset Risks** (limitations or concerns inherent to WinoPron itself):
- Does not cover all possible linguistic or cultural contexts
- Limited to constructed templates and evaluated pronoun sets

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**:  
Evaluation includes pronoun sets:  
- he/him/his  
- she/her/her  
- singular they/them/their  
- neopronoun xe/xem/xyr  
to address gender diversity beyond the binary, which is missing in much prior work on coreference bias.

**Potential Harm**: Potential misrepresentation of model capabilities due to bias in training data or limited linguistic scope.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not contain any personal identifiable information.

**Data Licensing**: AGPL-3.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All data creation followed ethical guidelines.
