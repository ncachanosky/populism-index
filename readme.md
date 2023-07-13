# Latin America (left-leaning) Populism Index Project

## The Index

The index has two sub-indices: (a) Economic populism $(EP)$ and (b) Institutional populism $(IP)$. Both sub-indices range from 0 (less) to 100 (more) populism.

Each sub-index is the interaction of populism policies with populist motives. Take, for instance, income distribution. This is a typical left-leaning populist policy, but not all of income distribution policies are carried by populist regimes. A high populist index requires a populist policy (such as income distribution) executed for populist reasons.

$$
\mathcal{I} = \frac{EP + IP}{2}
$$

where:

$$
\begin{align*}
EP &= \text{Populist rhetoric} \times \text{Populist economic policies} \\
IP &= \text{Populist rhetoric} \times \text{Populist institutional policies}
\\end{align*}
$$

## Economic Populism $(EP$)

### Budget Deficits

### Public Debt

### Inflation Rate

### Redistribution:

1) Relative redistribution. Measures the extent to which governments use taxes and transfers to redistribute income by comparing income inequality in the market to post-tax, post-transfer inequality.

Formula: $\frac{Gini_{Market} - Gini_{Post}}{Gini_{Market}}$

Source: The Standardized World Income Inequality Database (Solt, 2020). 

## Institutional Populism $(IP)$

### Rule of Law

$IP_1 = \text{v2x-rule} \cdot 100$

<!--
V-Dem rule of law components:
1. Compliance with high court                    - v2juhccomp
2. Complance with judiciary                      - v2jucomp
3. High court independence                       - v2juhcind
4. Lower court independence                      - v2juncind
5. Transparent laws with predictable enforcement - v2cltrnslw
6. Access to justice for men                     - v2clacjstm
7. Access to justice for women                   - v2clacjstw
8. Judicial accountability                       - v2juaccnt
9. Judicial corruption decision                  - v2jucorrde
10. Public sector corrupt exchanges              - v2xcrptps
11. Public sector theft                          - v2xthftps
12. Executive bribery and corrupt exchanges      - v2exbribe
13. Executive embezzlement and theft             - v2exembez

-->

### Executive power

<!--
V-Dem neopatrimonialism components:
1. Vote buyins - v2elvotbuy
2. Particularistic vs public goods                    - v2dlencmps
3. Party linkages                                     - v2psprlnks
4. Executive respects constitution                    - v2exrescon
5. Executive oversight                                - v2lgotovst
6. Legislature controls resources                     - v2lgfunds
7. Legislature investigates the executive in practice - v2lginvstp
8. High court independence                            - V2juhcind
9. Low court independence                             - v2juhcind
10. Compliance with high court                        - v2juhccomp
11. Compliance with judiciary                         - v2jucomp
12. Electoral managemente body autonomy               - v2elembaut
13. Executive embezzlement and theft                  - v2exembez
14. Executive bribes and corrput charges              - v2exbribe
15. Legislative corruption                            - v2lgcrrpt
16. Judicial corruption                               - v2jucorrde
-->

### Corruption

$IP_4 = \text{v2x-execorr} \cdot 100$

<!--
V-Dem executive corruption components:
1. Executive bribery      - v2exbribe
2. Executive embezzelment - v2xembez
-->

### Freedom of the Press

$$
IP_5 = 100 = \text{v2mecenefm_osp} \cdot 25
$$

## Sources

| VARIABLE                   | SOURCE        | VARIABLE CODE  |
| -------------------------- | ------------  | -------------- |
| **Institutional populism** |               |                |
| Rule of law                | [V-Dem][VDEM] | v2x_rule       |
| Neopatrimonialism          | [V-Dem][VDEM] | v2x_neopat     |
| Corruption                 | [V-Dem][VDEM] | v2x_execorr    |
| Freedom of expression      | [V-Dem][VDEM] | v2mecenefm_osp |



## References 
1. Solt, Frederick. 2020. “Measuring Income Inequality Across Countries and Over Time: The Standardized World Income Inequality Database.” Social Science Quarterly 101(3):1183-1199. SWIID Version 9.5, June 2023.



<!-- HYPERLINKS -->

[VDEM]: <https://www.v-dem.net/data/the-v-dem-dataset/>

