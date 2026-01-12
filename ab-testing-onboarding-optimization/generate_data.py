#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 18:30:54 2023

@author: johnpaulmbagwu
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate 50k users
n_users = 50000
user_ids = np.arange(1, n_users + 1)

# Variants: balanced 50/50
variants = np.random.choice(['control', 'treatment'], size=n_users, p=[0.5, 0.5])

# Acquisition channels: realistic split (organic 40%, paid social 30%, referral 20%, other 10%)
channels = np.random.choice(['organic', 'paid_social', 'referral', 'other'], 
                            size=n_users, p=[0.4, 0.3, 0.2, 0.1])

# Device types: mobile 60%, desktop 40%
devices = np.random.choice(['mobile', 'desktop'], size=n_users, p=[0.6, 0.4])

# Trial start dates: Q4 2025, spread over 4 weeks (Oct 1 - Oct 28)
start_date = datetime(2025, 10, 1)
trial_dates = [start_date + timedelta(days=random.randint(0, 27)) for _ in range(n_users)]

# Paid conversion: baseline ~12%, slight treatment lift overall (+0.3% to make it non-sig), bigger in mobile paid social
base_conv_prob = 0.12
treatment_lift = 0.003  # Tiny overall
paid_conversion_date = []
for i, (var, ch, dev) in enumerate(zip(variants, channels, devices)):
    prob = base_conv_prob
    if var == 'treatment':
        prob += treatment_lift
    # Boost for mobile paid social in treatment
    if var == 'treatment' and ch == 'paid_social' and dev == 'mobile':
        prob += 0.02  # +2% lift here
    if np.random.rand() < prob:
        # Convert within 30 days of trial start
        days_to_convert = random.randint(1, 30)
        conv_date = trial_dates[i] + timedelta(days=days_to_convert)
        paid_conversion_date.append(conv_date)
    else:
        paid_conversion_date.append(None)

# Session count 7d: Poisson around mean 4-6, slight treatment bump
lambda_control = 4.5
lambda_treatment = 4.8
session_counts = np.where(variants == 'control', 
                          np.random.poisson(lambda_control, n_users),
                          np.random.poisson(lambda_treatment, n_users))

# Avg session length: normal around 8 min, sd=2
avg_lengths = np.clip(np.random.normal(8, 2, n_users), 1, 30)

# Retention 7d: binary, 65% base, if session_count > 0
retention_7d = (session_counts > 0) & (np.random.rand(n_users) < 0.65)

# Derive paid_conversion binary for notebook
paid_conversion = [1 if date is not None else 0 for date in paid_conversion_date]

# Build DF
df = pd.DataFrame({
    'user_id': user_ids,
    'variant': variants,
    'acquisition_channel': channels,
    'device_type': devices,
    'trial_start_date': trial_dates,
    'paid_conversion_date': paid_conversion_date,
    'session_count_7d': session_counts,
    'avg_session_length_min': avg_lengths,
    'paid_conversion': paid_conversion,  # Derived for easy use
    'retention_7d': retention_7d  # Derived
})

# Save to CSV
df.to_csv('ab_test_data.csv', index=False)
print(f"Generated ab_test_data.csv with {len(df)} rows. Overall conv rate: {df['paid_conversion'].mean():.3f}")
print("Control conv: ", df[df['variant']=='control']['paid_conversion'].mean())
print("Treatment conv: ", df[df['variant']=='treatment']['paid_conversion'].mean())
