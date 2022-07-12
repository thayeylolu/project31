# Data Science for All by Correlation One - Project 31
# Summer 2022 Cohort
## Problem

Abortions are a medical procedure used to terminate pregnancy [1]. Globally, less than a third (29%) of all pregnancies terminate in abortions. Abortions are undertaken for multiple reasons. If the procedure is performed by a qualified medical professional, it can be a safe procedure with manageable risks. While the legislations governing abortion vary by district and country, the World Health Organization affirmed in 2020 the importance of safe, comprehensive abortion care through its inclusion in the list of essential health services [2].  

## Why this is interesting and important

In 24 countries, abortions are prohibited under any circumstances. Abortion bans do not eliminate abortions [3]. Instead, there is an associated rise in unsafe abortions, obtained outside the safety of medical facilities, with a much higher risk of death. Majority of individuals who are likely to get an abortion in the United States are women of color or from underrepresented communities [4],  and limited access to safe abortions has long-term effects on mental health and socio-economic wellbeing [5]. Hence, the reversal of the Roe vs. Wade ruling by the US Supreme Court curbs abortion access for women, and has significant implications for women’s health. The access and respect to women’s health care is at a significant decline in the U.S. It is important to understand the implications of policies that affect the health and well-being of women. 

## Proposal 
Abortion bans increase the likelihood of unsafe abortions, which negatively impact women’s health, and the recent US abortion ban is misaligned with the opinions of the general public. The goal of this project is twofold: using Bayesian regression modeling, to examine country-level trends in safe and unsafe abortions based on the presence or absence of an abortion ban, and examine public opinion by performing sentiment analysis on public tweets related to opinions regarding the recent US Supreme Court ruling.  We will use a Naive Bayes Classifier to perform natural language processing on text extracted from the tweets. We will also investigate the correlation between sentiment and location.

## Data

**Country-level data**

*Research question: “How are abortion bans related to the incidence of unsafe abortions?”*
1. Dataset from this research article:  Ganatra, B., Gerdts, C., Rossier, C., Johnson, B. R., Jr, Tunçalp, Ö., Assifi, A., Sedgh, G., Singh, S., Bankole, A., Popinchalk, A., Bearak, J., Kang, Z., & Alkema, L. (2017). Global, regional, and subregional classification of abortions by safety, 2010-14: estimates from a Bayesian hierarchical model. Lancet (London, England), 390(10110), 2372–2381. https://doi.org/10.1016/S0140-6736(17)31794-4
2. Categorical data (Abortion Bans: Present vs Absent) from: Guttmacher Institute. (n.d.). Global Abortion Incidence Dataset. https://osf.io/5k7fp/

**Twitter data**

*Research question: “What are trends in the opinion of Twitter users on abortions in the US - pro-life vs pro-choice? How have these trends changed prior to and after the reversal of the Roe v Wade ruling?"*
1. Categorized opinion tweets dataset (model training set) via SurgeAI
2. Data mining tweets with geolocation and timestamp attributes, pre-and-post reversal of the Roe v Wade ruling (test set) 
3. Download tweets dataset with geolocation and timestamp data, pre-and-post reversal of the Roe v Wade ruling (test set) via the Twitter API once the pending “Academic Research” application is approved.  If we do not receive approval, we will use the dataset available here: https://www.kaggle.com/datasets/nicolemichelle/abortion-ban-twitter-dataset (5000 rows of data)


## References
1. Bearak, J., Popinchalk, A., Ganatra, B., Moller, A. B., Tunçalp, Ö., Beavin, C., Kwok, L., & Alkema, L. (2020). Unintended pregnancy and abortion by income, region, and the legal status of abortion: estimates from a comprehensive model for 1990-2019. The Lancet. Global health, 8(9), e1152–e1161. https://doi.org/10.1016/S2214-109X(20)30315-6
2. World Health Organization. (2021). Abortion. https://www.who.int/news-room/fact-sheets/detail/abortion
3. Center for Reproductive Rights. (2021). The World’s Abortion Laws: Interactive Database. https://reproductiverights.org/maps/worlds-abortion-laws/?category[1348]=1348
4. Kortsmit, K., Mandel, M. G., Reeves, J. A., Clark, E., Pagano, H. P., Nguyen, A., Petersen, E. E., & Whiteman, M. K. (2021). Abortion Surveillance - United States, 2019. Table 6. Number of reported abortions, by known race/ethnicity and reporting area of occurrence — selected reporting areas,* United States, 2019. Morbidity and mortality weekly report. Surveillance summaries (Washington, D.C. : 2002), 70(9), 1–29. https://doi.org/10.15585/mmwr.ss7009a1
5.  Society of Behavioral Medicine. (2022). Position Statement: Protect Abortion Rights. https://www.sbm.org/UserFiles/ProtectAbortionRights.pdf
