gen t =_n
tsset t
list t
arch mpg price, earch(1/1) egarch(1/1)
predict h_mpg, variance eq(mpg, mpg)
arch mpg price, earch(1/1) egarch(1/1)
predict ITgarch, variance
tsline ITgarch
tsline ITgarch
test [ARCH]L.arch + [ARCH]L.garch == 1
gen date = m(2004m1) +_n-1
format date %tm
mgarch dcc (exchrtn = asirtn, arch(1/1) garch(1/1))
mgarch dcc ( exchrtn asirtn = L.exchrtn L.asirtn ), arch(1) garch(1) nolog vsquish
ardl asirtn exchrtn
ardl asirtn exchrtn,ec
ssc install ardl
findit ardl
ssc describe k
ssc describe kssur
install ksur
import excel "C:\Users\ACER\Desktop\GARCH 1,1.xlsx", sheet("Sheet1")
 net install ksur
 net install kssur
findit pkgname
ssc describe p
ksur ASI , maxlag(3)
ksur ASI
kssur ASI , maxlag(3)
kssur ASI
xtset CODE YEAR
xtunitroot ips GDP, lags(1)
xtunitroot ips d.GDP, lags(1)
xtunitroot llc REMITTANCE , lags(1)
gen ASIRTNsqrt=sqrt( ASIRTN)
gen ASIRTNlog=log( ASIRTN)
gen LNASIRTN=ln( ASIRTN)
gen ASIRTNexp=exp( ASIRTN)
gen ASIRTNsqr= ASIRTN^2
gen ASIRTNcube= ASIRTN^3
gen ASIRTNinv= 1/ASIRTN
gen ASIRTNabs=abs(ASIRTN)
twoway (tsrline ASIRTN EXCHRTN), ytitle(MACRO) ttitle(MICRO) title("ECO")
var oilprice exchrtn asirtn
irf create myirf , set(myirfs)
irf graph oirf , impulse( oilprice) response ( exchrtn asirtn)
irf table oirf , impulse( oilprice) response ( exchrtn asirtn)
irf table fevd , impulse( oilprice) response ( exchrtn asirtn)
irf graph fevd , impulse( oilprice) response ( exchrtn asirtn)
irf graph fevd , impulse( oilprice) response ( exchrtn asirtn)
