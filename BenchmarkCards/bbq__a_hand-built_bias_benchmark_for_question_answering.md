<div align="center">

# BBQ: A Hand-Built Bias Benchmark for Question Answering

<small><em>Original: 2110.08193v2.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

<p>
<img src="https://img.shields.io/badge/QuestionAnswering-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Question Answering" style="margin-right:5px;">
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
BBQ: A Hand-Built Bias Benchmark for Question Answering
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
BBQ is a dataset of question sets that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. It evaluates model responses in terms of how strongly they reflect social biases and under what contexts these biases override correct answers.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Dataset
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
<li>Question Answering</li>
<li>Natural Language Processing</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>English</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
<ul>
<li>UnQover</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="https://github.com/nyu-mll/BBQ">GitHub Repository</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To provide researchers a benchmark for measuring social biases in question answering models.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>NLP researchers</li>
<li>AI practitioners</li>
<li>Ethics researchers</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Evaluate biases in QA model outputs</li>
<li>Identify contexts that lead to biased outputs</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
The dataset focuses on biases relevant to the U.S. context and may not generalize to different cultural settings.
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
<ul>
<li>Generalizing results to non-U.S. languages or contexts</li>
</ul>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
Constructed by authors
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
58,492 unique examples
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
Templates of questions and contexts
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
Validated by crowdworkers
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Quantitative analysis of model outputs</li>
<li>Bias scoring based on model answers</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Accuracy</li>
<li>Bias score</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Bias scores reflect the percent of non-UNKNOWN outputs that align with a social bias.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
A bias score of 0% indicates no bias, while 100% indicates total alignment with social bias.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
N/A
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Human validation with a minimum agreement threshold of 4/5 annotators.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Stereotyping behavior</li>
<li>Reinforcement of social biases</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias</li>
<li><strong>Societal Impact:</strong> Impact on affected communities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Tested biases against various social categories including gender, race, socioeconomic status.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Reinforcement of harmful stereotypes in model outputs.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Released under the CC-BY 4.0 license.
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