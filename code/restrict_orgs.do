set more off

/*open log*/
log using "/ifs/gsb/mcorrito/gd_contractors/output/restrict_orgs_stats.log",replace text
log off

/*import extract csv*/
import delimited "/tmp/extract.csv",bindquotes(strict) varnames(1) colrange(1:11) clear 

destring reviewid orgid,replace force

egen orgid2=group(orgid)
egen reviewid2=group(reviewid)

log on
display("Distinct Records")
summarize
log off
drop orgid2 reviewid2
    
/*create date vars*/    
split datetime
drop datetime2
split datetime1,p("-")
ren datetime11 year
ren datetime12 month
destring year,replace
drop datetime* month

drop if reviewid == -1
duplicates drop reviewid,force    

/*create master review IDs for orgs w/at least 25 */
/*reviews/year for at least one year*/
bysort orgid year: g numReviews = _N
drop if numReviews<25 

egen orgid2=group(orgid)
egen reviewid2=group(reviewid)
summarize
drop orgid2 reviewid2
sort orgid year
export delimited "/ifs/gsb/mcorrito/gd_contractors/data/master_orgIDs_annual.csv",replace

log close






