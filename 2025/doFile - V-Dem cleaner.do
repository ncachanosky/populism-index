/* =============================================================================
*| LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA
*|
*| V-Dem Cleaner
*| Nicolas Cachanosky
*| Center for Free Enterprise
*| The University of Texas at El Paso
*| ncachanosky@utep.edu
*| www.ncachanosky.com
*| 
*| J. P. Bastos
*| Free Market Institute
*| Texas Tech University
*| jpmvbastos@gmail.com
*| https://www.jpmvbastos.com/
*| 
*| Version: 1.0
*| Last update: 08-Mar-2025
*| 
*| Target: V-Dem dataset size < 100M
*/ ============================================================================

*| MANUALLY LOAD V-DEM

*| KEEP NEEDED VARIABLES
global keep1 = "country_text_id year "
global keep2 = "v2x_rule v2x_jucon v2xlg_legcon v2x_execorr v2x_neopat v2mecenefm_osp"

keep $keep1 $keep2

*| DROP OBSERVATIONS PRIOR TO 1990 AND AFTER 2020
drop if year < 1990
drop if year > 2020


*| SAVE DATA
save "C:\Users\ncachanosky\OneDrive\Research\populism-index\2025\Data\V-Dem-13.dta", replace