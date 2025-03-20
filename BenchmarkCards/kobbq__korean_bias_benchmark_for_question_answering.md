<div align="center">

# KoBBQ: Korean Bias Benchmark for Question Answering

<small><em>Original: 2307.16778v2.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

<p>
<img src="https://img.shields.io/badge/SocialBias-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Social Bias" style="margin-right:5px;">
<img src="https://img.shields.io/badge/CulturalAdaptation-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Cultural Adaptation" style="margin-right:5px;">
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
KoBBQ: Korean Bias Benchmark for Question Answering
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
KoBBQ is a dataset designed to evaluate social biases of language models (LMs) in the Korean context, adapting the English BBQ benchmark to reflect cultural nuances unique to South Korea.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Question-Answering
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
<li>Social Bias</li>
<li>Cultural Adaptation</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>Korean</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
<ul>
<li>BBQ</li>
<li>CBBQ</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="https://jinjh0123.github.io/KoBBQ">Resource</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To measure and analyze social biases in Korean language models through a culturally adapted benchmark.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>Researchers</li>
<li>Developers of LMs</li>
<li>Social scientists</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Evaluate bias in LMs</li>
<li>Assess accuracy in QA tasks</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
The perception of social bias can be subjective; further research is needed to explore other bias categories.
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
<ul>
<li>Training models to generate biased content</li>
<li>Non-research related applications</li>
</ul>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
KoBBQ Dataset
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
76,048 samples
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
Multiple-choice QA format
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
Templates and samples reflect cultural biases in South Korea
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Large-scale survey for bias validation</li>
<li>Cultural-sensitive translation</li>
<li>Template categorization</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Accuracy</li>
<li>Bias score</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Accuracy is calculated based on correct responses given ambiguous and disambiguated contexts. Bias scores measure model tendencies toward biased answers.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Higher accuracy correlates with lower bias scores; a balanced assessment combines both aspects.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Templates validated through a survey of 100 South Koreans for demographic representation.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Cultural bias</li>
<li>Translation inaccuracies</li>
<li>Representation of stereotypes</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias, Output bias</li>
<li><strong>Accuracy:</strong> Poor model accuracy</li>
<li><strong>Transparency:</strong> Lack of training data transparency</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Demographic details were collected to ensure broad representation in survey validation.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Misinterpretations of the biases could perpetuate stereotypes or reinforce biases in LMs.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Participants in surveys were ensured privacy and anonymity.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Dataset usage is restricted to non-malicious applications.
</td></tr>
<tr><td width="20%" align="center"><strong>Consent Procedures</strong></td><td>
Informed consent was obtained from all participants involved in the survey.
</td></tr>
<tr><td width="20%" align="center"><strong>Compliance With Regulations</strong></td><td>
Study conducted under approval from KAIST IRB.
</td></tr>
</table>

<hr>

<div align="center">
<p><em>This benchmark card was automatically generated.</em></p>
</div>