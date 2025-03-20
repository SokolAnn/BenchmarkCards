<div align="center">

# WinoBias

<small><em>Original: N18-2003.json</em></small>

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
WinoBias
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
A benchmark for coreference resolution focused on gender bias using Winograd-schema style sentences with entities corresponding to people referred by their occupation.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Text
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
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
<li>Ontonotes</li>
<li>CoNLL-2011</li>
<li>CoNLL-2012</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="http://winobias.org">Resource</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To evaluate and mitigate gender bias in coreference resolution systems.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>Researchers</li>
<li>Developers in Natural Language Processing</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Coreference Resolution</li>
<li>Bias Evaluation</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
WinoBias dataset created by researchers familiar with the project.
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
3,160 sentences
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
Text
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
Sentences created with equal numbers of correct co-reference decisions for all occupations.
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Rule-based</li>
<li>Feature-rich</li>
<li>Neural Coreference System</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>F1 Score</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Average difference in F1 score between pro-stereotyped and anti-stereotyped conditions.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Systems must link gendered pronouns to pro-stereotypical and anti-stereotypical occupations equally well.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Demonstrated through comparison with established datasets like OntoNotes.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Bias in training data</li>
<li>Underrepresentation of female entities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias</li>
<li><strong>Accuracy:</strong> Poor model accuracy</li>
<li><strong>Robustness:</strong> Prompt leaking</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Underrepresentation of female references in training datasets.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Amplification of gender stereotypes through biased predictions.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Data includes references to occupations and gendered pronouns, anonymized to mitigate bias.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Not Applicable
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