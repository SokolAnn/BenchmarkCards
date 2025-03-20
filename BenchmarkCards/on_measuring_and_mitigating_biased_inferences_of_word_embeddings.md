<div align="center">

# On Measuring and Mitigating Biased Inferences of Word Embeddings

<small><em>Original: 1908.09369v3.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

<p>
<img src="https://img.shields.io/badge/NaturalLanguageProcessing-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Natural Language Processing" style="margin-right:5px;">
</p>

</div>

## Table of Contents

- [📊 Benchmark Details](#-benchmark-details)
- [🎯 Purpose and Intended Users](#-purpose-and-intended-users)
- [💾 Data](#-data)
- [🔬 Methodology](#-methodology)
- [⚠️ Targeted Risks](#️-targeted-risks)
- [🔒 Ethical and Legal Considerations](#-ethical-and-legal-considerations)

<hr>

## 📊 Benchmark Details

<table>
<tr><td width="20%" align="center"><strong>Name</strong></td><td>
On Measuring and Mitigating Biased Inferences of Word Embeddings
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
This paper explores the stereotypes encoded in word embeddings and their impact on natural language inference (NLI) tasks, proposing a mechanism to measure and mitigate such biases.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Word embeddings
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
<li>Natural Language Processing</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>N/A</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
<ul>
<li>N/A</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="arXiv:1908.09369v3">Resource</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To measure and mitigate biased inferences in word embeddings using natural language inference tasks.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>Researchers in NLP</li>
<li>Developers working on bias in AI</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Natural Language Inference</li>
<li>Bias measurement</li>
<li>Bias mitigation</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
The study primarily focuses on gender bias and may not cover all biases comprehensively.
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
<ul>
<li>Applications beyond NLP</li>
</ul>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
SNLI dataset
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
Large (contains millions of sentence pairs)
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
Text
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
NLP tasks tagged with entailment relationships
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Natural Language Inference (NLI)</li>
<li>Debiasing via projection method</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Net Neutral (NN)</li>
<li>Fraction Neutral (FN)</li>
<li>Threshold measures</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Calculated bias from model probabilities of entailment, contradiction, or neutrality.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Scores close to 1 indicate low bias, while lower scores represent higher bias.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
GloVe, ELMo, and BERT embeddings exhibit substantial biases.
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Evaluation against standard benchmarks in natural language inference tasks.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Gender bias</li>
<li>Religion bias</li>
<li>Nationality bias</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias</li>
<li><strong>Value Alignment:</strong> Toxic output</li>
<li><strong>Robustness:</strong> Hallucination</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Examined through gender, nationality, and religious attributes.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Invalid inferences leading to potential reinforcement of stereotypes.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
The licensing for the SNLI dataset is publicly available.
</td></tr>
<tr><td width="20%" align="center"><strong>Consent Procedures</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Compliance With Regulations</strong></td><td>
Not Applicable
</td></tr>
</table>

<hr>

<div align="center">
<p><em>This benchmark card was automatically generated.</em></p>
</div>