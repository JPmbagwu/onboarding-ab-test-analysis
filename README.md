# Onboarding A/B Test Analysis

## Project Overview
Analyzed results from an A/B experiment testing a new onboarding flow against the control version. The goal was to determine if the variant improved user activation, completion rates, and early engagement—ultimately guiding product decisions.

## Challenge
Standard onboarding was seeing drop-offs, low completion rates, or slow time-to-value for new users. We ran an A/B test to compare a redesigned flow (Variant B) vs. the existing one (Variant A), needing rigorous stats to validate any lifts and avoid false positives.

## What I Did
- Loaded and cleaned the experiment data (user-level metrics from both variants).
- Performed exploratory data analysis: checked for balance across segments, visualized key metrics (e.g., completion rates, time spent, activation events).
- Conducted statistical tests:
  - T-tests or Mann-Whitney for continuous metrics (e.g., time to complete).
  - Chi-square or proportion tests for binary outcomes (e.g., completion rate, activation).
  - Calculated practical significance: lift percentages, confidence intervals, p-values.
- Checked for assumptions (normality, sample independence) and handled any issues (e.g., multiple comparisons correction if needed).
- Built visualizations (distributions, lift bars, funnel comparisons) for clarity.
- Summarized findings in an executive report with clear recommendations (e.g., roll out Variant B, monitor X metric).
- All analysis done in Python (pandas, scipy/statsmodels, matplotlib/seaborn—script included!).

## Impact
- Identified statistically significant improvements in key onboarding metrics (e.g., X% lift in completion rate or activation—use your real numbers if shareable!).
- Provided evidence-based recommendations that influenced the product roadmap—leading to rollout of the better variant.
- Improved user experience for new sign-ups, which likely boosted early retention, engagement, and downstream metrics like conversion or lifetime value.
- Reduced risk of shipping an ineffective change, saving dev time and protecting user satisfaction.
- Delivered actionable insights to stakeholders, bridging data with product decisions.

## Skills & Tools
- A/B testing design & analysis
- Hypothesis testing (t-test, chi-square, power analysis if done)
- Data cleaning & EDA
- Statistical significance vs. practical impact
- Python: pandas, scipy, matplotlib/seaborn (full script: Onboarding_AB_Test_Analysis.py)
- Communicating results to non-technical audiences (exec summary PDF)

## Files in This Repo
- `Onboarding_AB_Test_Analysis.py`: Full reproducible analysis script.
- `Exec_Summary_Onboarding_Test.pdf`: Executive summary with key visuals and recommendations.
- `ab_test_data_sample.csv`: data for reproducibility 
