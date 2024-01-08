# Latin America Left-Leaning Populism Index Project

> :small_red_triangle: PROJECT UNDER DEVELOPMENT :small_red_triangle:

## The Index

### Introduction

The **Latin America Left-Leaning Populism Index** is a measure of active populist policies. The index has two sub-indices:

* Economic populism $(EP)$
* Institutional populism $(IP)$.

Eash sub-index is the result of interacting a measure of populist *rhetoric* with typical left-leaning policies. This interaction produces two outcomes:

* Take into consideration if populist *rhetoric* becomes *action*
* Take into consideration if typical populist policies are executed for *populist reasons*

Each sub-index is the interaction of populism policies (economic or institutional) with populist motives $(POP)$. Take, for instance, income distribution. This is a typical left-leaning populist policy, but not all of income distribution policies are carried by populist regimes. A high populist index requires a populist policy (such as income distribution) executed for populist reasons. To achieve this, the index interacts economics and institutional policies with a measure of populist rhetoric.

Each sub-index is constructed with a number of components. All components are adjusted to range between 0 (less) to 100 (more) populism.

By interacting populist policies with populist rhetoric (motives), the index separates non-populist regimes that carry out populist policies and populist regimes that do not carry out populist policies. Because the index can be dissagregated, its information can be used to study:

1. The effects of populism (the overall index)
2. The effects of economic populism
3. The effects of institutinal populism
4. The effects of economic populist policies carried out by a non-populist regime
5. The effects of institional populist policies carried out by a non-populist regime
6. The effects of a populist regime that does not carry out populist policies

### Methodology

The index is the arithmetic average of $EP$ and $IP$ adjusted for a measure of populist motives.

$\mathcal{I} = \frac{(\text{Populist rhetoric} \times \text{Populist economic policies}) + (\text{Populist rhetoric} \times \text{Populist institutional policies})}{2}$

$\mathcal{I} = \frac{(POP \cdot EP) + (POP \cdot IP)}{2} = P \cdot \left(\frac{EP + IP}{2}\right)$

Where `POP` is a measure of populist rhetoric and `EP` and `IP` denote economic and institutional populistm respectively.

Subsequently, each sub-index is the arithmetic average of their components.

### Populism rhetoric

The measure of *populism rhetoric* is the V-Party Populism index. The index data is re-escale from (0, 1) to (0, 100). 

The V-Party Populism Index measures the populist rhetoric of active political parties in each country. The index uses the index corresponding to the head of state's political party affiliation. For years where there is a change of party in the executive office, the data for the party with majority of days in office is used.

### Economic Populism $(EP)$

The Economic Populism Sub-Index looks at the following four (4) economic policy areas typically observed in Latin American populist regimes:

1. Business (and labor market) regulations
2. Government interference
3. Monetary (and financial) freedom
4. Freedom to trade (internationally)

$
EP = P \cdot \left(\frac{\text{Business regulations + Gov. interferences + Monetary freedom + Freedom to trade}}{4}\right)
$

$
EP = P \cdot \left(\frac{EP_1 + EP_2 + EP_3 + EP_4}{4}\right)
$

The contributors to each economic policy area are the following

* EP$_1 = \frac{EP_{11} + EP_{12} + EP_{13}}{3}$
* EP$_2 = \frac{EP_{21} + EP_{22}}{2}$
* EP$_3 = \frac{EP_{31} + EP_{32} + EP_{33}}{3}$
* EP$_4 = \frac{EP_{41} + EP_{42}}{3}$

where:

* EP$_{11}$ = Heritage's Foundation Index of Economic Freedom: Business freedom.
* EP$_{12}$ = Fraser's Economic Freedom of the World: Labor Market Regulations (5A).
* EP$_{13}$ = Fraser's Economic Freedom of the World: Business Regulations (5C).
* EP$_{21}$ = Fraser's Economic Freedom of the World: Transfers and Subsidies (1B).
* EP$_{22}$ = Fraser's Economic Freedom of the World: State Ownership (IE).
* EP$_{31}$ = Heritage's Foundation Index of Economic Freedom: Monetary Freedom.
* EP$_{32}$ = Heritage's Foundation Index of Economic Freedom: Financial Freedom.
* EP$_{33}$ = Fraser's Economic Freedom of the World: Foreign Currency and Bank Accounts (3D).
* EP$_{41}$ = Heritage's Foundation Index of Economic Freedom: Trade Freedom.
* EP$_{42}$ = Fraser's Economic Freedom of the World: Freedon to Trade Internationally (4).

### Institutional Populism $(IP)$

The Institutional Populism Sub-Index looks at the following five (5) institutional areas typically observed in Latin American populist regimes:

1. Rule of Law
2. Corruption
3. Neopatrimonialism
4. Freedom of the Expression
5. Property Rights


$
IP = \frac{\text{Rule of Law + Corruption + Neopatrimonialism + Freedom of Expression + Property Rights}}{5}
$

$
IP = \frac{IP_1 + IP_2 + IP_3 + IP_4 + IP_5}{5}
$

The contributors to each economic policy area are the following

* IP$_1 = \frac{IP_{11} + IP_{12} + IP_{13} + IP_{14}}{4}$
* IP$_2 = \frac{IP_{21} + IP_{22}}{2}$
* IP$_3 = IP_{31}$
* IP$_4 = IP_{41}$
* IP$_5 = IP_{51}$

where:

* IP$_{11}$ = V-Dem: Rule of Law.
* IP$_{12}$ = V-Dem: Judiciary Constraints on the Executive.
* IP$_{13}$ = V-Dem: Legislative Constraints on the Executive.
* IP$_{14}$ = WGI: Rule of Law.
* IP$_{21}$ = V-Dem: Corruption.
* IP$_{22}$ = WGI: Control of Corruption.
* IP$_{31}$ = V-Dem: Neopatrimonialism.
* IP$_{41}$ = V-Dem: Freedom of Expression.
* IP$_{51}$ = Heritage's Foundation Index of Economic Freedom: Property Rights.


## Sources

The folling tables includes the source of each component used in the index and its original databse `code name`.

| Variable                                           | Source                               | Variable code     |
| -------------------------------------------------- | ------------------------------------ | ----------------- |
| **Populism rhetorical index**                      |                                      |                   |
| Populism index                                     | [V-Dem][VDEM1]                       | v2xpa_popul       |
| **Economic populism**                              |                                      |                   |
| EP$_{11}$: Business Freedom                        | [Index of Economic Freedom][HIEF]    | Business Freedom  |
| EP$_{12}$: Labor Markert Regulations               | [Economic Freedom of the World][EFW] | 5A                |
| EP$_{13}$: Business Regulations                    | [Economic Freedom of the World][EFW] | 5C                |
| EP$_{21}$: Transfers and Subsidies                 | [Economic Freedom of the World][EFW] | 1B                |
| EP$_{22}$: State Ownership                         | [Economic Freedom of the World][EFW] | IE                |
| EP$_{31}$: Monetary Freedom                        | [Index of Economic Freedom][HIEF]    | Monetary Freedom  |
| EP$_{32}$: Financial Freedom                       | [Index of Economic Freedom][HIEF]    | Financial Freedom |
| EP$_{33}$: Foreign Currency and Bank Accounts      | [Economic Freedom of the World][EFW] | 3D                |
| EP$_{41}$: Trade Freedom                           | [Index of Economic Freedom][HIEF]    | Trade Freedom     |
| EP$_{42}$: Freedom to Trade Internationally        | [Economic Freedom of the World][EFW] | 4                 |
| **Institutional populism**                         |                                      |                   |
| IP$_{11}$: Rule of law                             | [V-Dem][VDEM2]                       | v2x_rule          |
| IP$_{12}$: Judiciary Consraints on the Executive   | [V-Dem][VDEM2]                       | v2x_jucon         |
| IP$_{13}$: Legislative Consraints on the Executive | [V-Dem][VDEM2]                       | v2xlg_legcon      |
| IP$_{14}$: Rule of Law                             | [World Governance Indicators][WGI]   | RL_EST            |
| IP$_{21}$: Corruption                              | [V-Dem][VDEM2]                       | 2x_execorr        |
| IP$_{22}$: Control of Corruption                   | [World Governance Indicators][WGI]   | CC_EST            |
| IP$_{31}$: Neopatrimonialism                       | [V-Dem][VDEM2]                       | 2x_neopat         |
| IP$_{41}$: Freedom of Expression                   | [V-Dem][VDEM2]                       | v2mecenefm_osp    |
| IP$_{51}$: Property Rights                         | [Index of Economic Freedom][HIEF]    | Property Rights   |




<!-- HYPERLINKS -->
[VDEM1]: <https://v-dem.net/data/v-party-dataset/>
[VDEM2]: <https://www.v-dem.net/data/the-v-dem-dataset/>
[HIEF] : <https://www.heritage.org/index/>
[EFW]  : <https://www.fraserinstitute.org/economic-freedom/map>
[WGI]  : <https://info.worldbank.org/governance/wgi/>



